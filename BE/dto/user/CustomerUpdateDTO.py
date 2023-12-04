from datetime import date
from typing import Optional
from pydantic import BaseModel


class CustomerUpdateDTO(BaseModel):
    id: int
    code: Optional[str]
    name: Optional[str]
    gender: Optional[str]
    number_phone: Optional[str]
    address: Optional[str]
    avatar: Optional[str]
    date_of_birth: date
    point: int
    