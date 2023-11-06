from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class AccountDTO(BaseModel):
    username: str
    password: str
