from dataclasses import dataclass
from sqlalchemy import Column, Integer, String

from model.BaseModel import BaseModel


class EmployeeType(BaseModel):
    __tablename__ = 'employee_type'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50))