from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Data(SqlAlchemyBase, SerializerMixin):
    __tablename__ == "computers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    local = Column(String, nullable=True)
    local_count = Column(Integer, default=0)
    usb = Column(String, nullable=True)
    usb_count = Column(Integer)

