from pydantic import BaseModel


class ImageCreateDTO(BaseModel):
    name: str
