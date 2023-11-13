from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class RegistrationDataDTO(BaseModel):
    email: EmailStr = ...
    username: Optional[str] = Field(..., min_length=3, max_length=30)
    password: Optional[str] = Field(..., min_length=5, max_length=30)
