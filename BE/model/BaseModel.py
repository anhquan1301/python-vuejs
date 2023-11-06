from dataclasses import dataclass
from sqlalchemy import Column, DateTime, func

from config.db import Base

class BaseModel(Base):
    __abstract__ = True
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
