from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Phone(SqlAlchemyBase, SerialazerMixin):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    remote = Column(String, nullable=True)
    remote_count = Column(Integer)
    usb = Column(String, nullable=True)
    usb_count = Column(Integer)
    bluetooth = Column(String, nullable=True)
    bluetooth_count = Column(Integer)

