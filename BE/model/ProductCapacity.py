from sqlalchemy import BigInteger, Column, Integer

from model.BaseModel import BaseModel


class ProductCapacity(BaseModel):
    __tablename__ = "product_capacity"
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(BigInteger)
    price_sale = Column(BigInteger)
    quantity = Column(Integer)
    capacity_id = Column(Integer)
    product_id = Column(Integer)
    color_id = Column(Integer, unique=True)
