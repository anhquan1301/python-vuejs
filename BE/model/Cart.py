from sqlalchemy import BigInteger, Column, Integer
from model.BaseModel import BaseModel


class Cart(BaseModel):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer)
    price = Column(BigInteger)
    capacity_product_id = Column(Integer)
    customer_id = Column(Integer)
