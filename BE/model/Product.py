from dataclasses import dataclass
from sqlalchemy import Boolean, Column, Integer, String, Text

from model.BaseModel import BaseModel


class Product(BaseModel):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(10))
    name = Column(String(50))
    description = Column(Text)
    is_data_entry = Column(Boolean, default=False)
    is_delete = Column(Boolean, default=False)
    product_type_id = Column(Integer, unique=True)
    producer_id = Column(Integer, unique=True)
    
