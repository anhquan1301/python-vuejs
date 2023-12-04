from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class CustomerCreateDTO(BaseModel):
    name: Optional[str] = Field(..., max_length=30)
    gender: bool
    number_phone: Optional[str] = Field(
        ..., min_length=10, max_length=12, alias="numberPhone"
    )
    address: Optional[str] = Field(...)
    avatar: Optional[str] = Field(
        default="https://inkythuatso.com/uploads/thumbnails/800/2023/03/9-anh-dai-dien-trang-inkythuatso-03-15-27-03.jpg"
    )
    date_of_birth: date = Field(..., alias="dateOfBirth")
