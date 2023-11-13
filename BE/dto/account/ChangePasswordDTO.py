from typing import Optional

from pydantic import BaseModel, Field


class ChangePasswordDTO(BaseModel):
    password: Optional[str] = Field(..., min_length=5, max_length=30)
    confirm_password: Optional[str] = Field(
        ..., min_length=5, max_length=30, alias="oldPassword"
    )
    new_password: Optional[str] = Field(
        ..., min_length=5, max_length=30, alias="newPassword"
    )
