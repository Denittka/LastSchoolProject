from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Router(SqlAlchemyBse, SerializerMixin):
    __tablename__ = "routers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    local = Column(String, nullable=True)
    local_count = Column(Integer)

