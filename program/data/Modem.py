from sqlalchemy import Column, Integer, String
from sqlalchemy-serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Modem(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "modems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    local = Column(String, nullable=True)
    local_count = Column(Integer)
    remote = Column(String, nullable=True)
    remote_count = Column(Integer)

