from sqlalchemy import Column, Integer, String, Text
from model.BaseModel import BaseModel


class Account(BaseModel):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50))
    username = Column(String(50))
    password = Column(Text)
    o_auth_provider = Column(String(20))
    otp_scret = Column(String(6))
