from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger, desc, func
from sqlalchemy.orm import relationship
from models.base import db, Base
from spider.yushu_book import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        return Wish.query.filter_by(
            uid=uid, launched=False).order_by(
            desc(Wish.create_time)
        ).all()

    @classmethod
    def get_gifts_counts(cls, isbn_list):
        from models.gift import Gift
        # 根据传入的一组 isbn， 到 Wish 表中计算出某个礼物的 Wish 心愿数量
        # filter  接受条件表达式
        # 没有 group_by 查出来的所有的数量，group_by 后返回一组列表
        count_list = db.session.query(func.count(
            Gift.id), Gift.isbn).filter(
            Gift.launched==False,
            Gift.isbn.in_(isbn_list),
            Gift.status==1).group_by(Gift.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first