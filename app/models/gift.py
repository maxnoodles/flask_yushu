from flask import current_app
from sqlalchemy import Column, Integer, String, Boolean, \
    Float, ForeignKey, SmallInteger, desc, func
from sqlalchemy.orm import relationship

from models.base import db, Base
from spider.yushu_book import YuShuBook


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    def is_yourself_gift(self, uid):
        return True if self.uid == uid else False

    @classmethod
    def get_user_gifts(cls, uid):
        return Gift.query.filter_by(
            uid=uid, launched=False).order_by(
            desc(Gift.create_time)
        ).all()

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from models.wish import Wish
        # 根据传入的一组 isbn， 到 Wish 表中计算出某个礼物的 Wish 心愿数量
        # filter  接受条件表达式
        # 没有 group_by 查出来的所有的数量，group_by 后返回一组列表
        count_list = db.session.query(func.count(
            Wish.id), Wish.isbn).filter(
            Wish.launched==False,
            Wish.isbn.in_(isbn_list),
            Wish.status==1).group_by(Wish.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 对象代表一个礼物，具体
    # 类代表礼物这个实物，它是抽象的，不是具体的“一个礼物”
    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']
        ).distinct().all()
        return recent_gift

