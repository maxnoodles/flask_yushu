from sqlalchemy import Column, Integer, String


# 继承 SqlAlchemy 的模型类
from models.base import db, Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=True)
    author = Column(String(30), default='未名')
    # 是否精装
    binding = Column(String(20))
    price = Column(String(20))
    # 出版社
    publisher = Column(String(50))
    pages = Column(Integer)
    # 出版时间
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass

