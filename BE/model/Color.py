from sqlalchemy import Column, Integer, String

from model.BaseModel import BaseModel


class Color(BaseModel):
    __tablename__ = "color"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    hex_code = Column(String(15))
