from dataclasses import dataclass
from sqlalchemy import Boolean, Column, Integer, Text

from model.BaseModel import BaseModel


class Image(BaseModel):
    __tablename__ = "image"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    product_capacity_id = Column(Integer)
    is_display = Column(Boolean, default=False)
