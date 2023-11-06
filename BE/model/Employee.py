from dataclasses import dataclass
from sqlalchemy import BigInteger, Column, Integer

from model.BaseModel import BaseModel
from model.User import User


class Employee(User):
    __tablename__ = 'employee'
    salary = Column(BigInteger)
    employee_type_id = Column(Integer)