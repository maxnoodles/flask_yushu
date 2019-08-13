from sqlalchemy import Column, Integer, SmallInteger, String

from libs.enums import PendingStatus
from models.base import Base


class Drift(Base):
    """
        一次具体交易信息
    """
    # 邮寄信息
    id = Column(Integer, primary_key=True)
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)

    # 书籍信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(40))
    book_image = Column(String(50))

    # 请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(String(50))

    # 赠送者信息
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))

    _pending = Column('pending', SmallInteger, default=1)

    @property
    def pending(self):
        return PendingStatus(self._pending)

    @pending.setter
    def pending(self, status):
        self._pending = status.value
