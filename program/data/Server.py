from sqlalchemy import Column, String, Integer
from sqlalchemy-serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Server(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "servers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    local = Column(String, nullable=True)
    local_count = Column(Integer)
    usb = Column(String, nullable=True)
    usb_count = Column(Integer)

