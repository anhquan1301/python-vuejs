from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from model.BaseModel import BaseModel


class Producer(BaseModel):
    __tablename__ = 'producer'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)