from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from settings.db import ENGINE, Base


class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)


class User(BaseModel):
    id: int
    name: str
    age: int
