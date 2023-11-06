from sqlalchemy.orm import relationship
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from config.db import Base

from model.BaseModel import BaseModel


class Role(BaseModel):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
