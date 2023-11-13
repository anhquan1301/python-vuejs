from typing import Optional
from pydantic import BaseModel, Field


class AccountDTO(BaseModel):
    username: Optional[str] = Field(..., min_length=5, max_length=30)
    password: Optional[str] = Field(..., min_length=5, max_length=30)
