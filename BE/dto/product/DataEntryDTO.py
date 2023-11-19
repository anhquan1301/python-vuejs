from pydantic import BaseModel, Field

from dto.product.CapacityProductCreateDTO import CapacityProductCreateDTO


class DataEntryDTO(BaseModel):
    product_id: int = Field(alias="productId")
    data_entry_list: list[CapacityProductCreateDTO] = Field(alias="dataEntryList")
