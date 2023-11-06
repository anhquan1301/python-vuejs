

from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from model.BaseModel import BaseModel


class Capacity(BaseModel):
    __tablename__ = 'capacity'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)