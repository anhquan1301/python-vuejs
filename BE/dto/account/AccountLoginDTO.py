from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class AccountDTO:
    username: str
    password: str
