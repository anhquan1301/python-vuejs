from sqlalchemy import BigInteger, Column, Integer
from model.BaseModel import BaseModel


class OrderDetail(BaseModel):
    __tablename__ = "order_detail"
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer)
    price = Column(BigInteger)
    subtotal = Column(BigInteger)
    order_product_id = Column(Integer)
    product_id = Column(Integer)
