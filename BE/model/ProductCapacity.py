from dataclasses import dataclass

from sqlalchemy import BigInteger, Column, Integer

from model.BaseModel import BaseModel


class Capacity(BaseModel):
    __tablename__ = 'product_capacity'
    id = Column(Integer,primary_key=True,autoincrement=True)
    price = Column(BigInteger)
    price_sale = Column(BigInteger)
    quantity = Column(Integer)
    