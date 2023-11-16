from typing import Optional
from pydantic import BaseModel, Field


class ProductCreateDTO(BaseModel):
    name: Optional[str]
    description: Optional[str]
    product_type_id: int = Field(alias="productTypeId")
    producer_id: int = Field(alias="producerId")
