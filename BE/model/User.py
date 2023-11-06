from dataclasses import dataclass
from sqlalchemy import Boolean, Column, Integer, String, Text
from model.BaseModel import BaseModel


class User(BaseModel):
    __abstract__ = True
    id = Column(Integer, primary_key=True,autoincrement=True)
    code = Column(String(50))
    name = Column(String(50))
    gender = Column(Boolean)
    number_phone = Column(String(10))
    address = Column(Text)
    avatar = Column(Text)
    date_of_birth = Column(String(50))
    account_id = Column(Integer)

    