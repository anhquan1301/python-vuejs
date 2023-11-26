from sqlalchemy import Column, Integer
from model.User import User


class Customer(User):
    __tablename__ = "customer"
    point = Column(Integer)
