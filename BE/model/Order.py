from sqlalchemy import BigInteger, Column, Integer, String, Text

from model.BaseModel import BaseModel


class Order(BaseModel):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(10))
    payment_method = Column(String(20))
    phone_number_of_the_buyer = Column(String(10))
    shipping_address = Column(Text)
    total_pay = Column(BigInteger)
    customer_id = Column(Integer)
