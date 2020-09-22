from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Laptop(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "laptops"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    remote = Column(String, nullable=True)
    remote_count = Column(Integer)
    local = Column(String, nullable=True)
    local_count = Column(Integer)
    usb = Column(String, nullable=True)
    usb_count = Column(Integer)
    bluetooth = Column(String, nullable=True)
    bluetooth_count = Column(Integer)

