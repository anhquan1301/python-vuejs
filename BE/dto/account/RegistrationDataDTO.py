from dataclasses import dataclass
from pydantic import BaseModel, constr, EmailStr


@dataclass
class RegistrationDataDTO(BaseModel):
    email: EmailStr
    username: str
    password: constr(min_length=5,max_length=30)
