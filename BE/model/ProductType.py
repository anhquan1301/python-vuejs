from dataclasses import dataclass
from sqlalchemy import Column, Integer, String

from model.BaseModel import BaseModel


class ProductType(BaseModel):
    __tablename__ = 'product_type'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)