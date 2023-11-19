from pydantic import BaseModel, Field

from dto.product.ImageCreateDTO import ImageCreateDTO


class CapacityProductCreateDTO(BaseModel):
    price: int
    price_sale: int = Field(alias="priceSale")
    quantity: int
    capacity_id: int = Field(alias="capacityId")
    product_id: int = Field(alias="productId")
    color_id: int = Field(alias="colorId")
    image_list: list[ImageCreateDTO] = Field(alias="imageList")
