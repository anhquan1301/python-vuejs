from http import HTTPStatus
from sqlalchemy.orm import scoped_session
from core.Enum import CodeName
from dto.product.ProductCreateDTO import ProductCreateDTO
from model.Product import Product

from repository.ProductRepository import ProductRepository
from common.Commons import Commons


class ProductService:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.product_repo = ProductRepository(db=self.db)
        self.commons = Commons(db=db)

    def get_product_list(self, value_search: dict) -> dict:
        result_product_list: list = self.product_repo.get_product_list(**value_search)
        response: dict = {"message": "Retrieve data successfully"}
        products: list = []
        for element in result_product_list:
            result: dict = {
                "id": element.product_id,
                "code": element.product_code,
                "name": element.product_name,
                "price": element.price,
                "priceSale": element.price_sale,
                "imageName": element.image_name,
            }
            products.append(result)
        response["data"] = products
        return self.commons.response_func_http(response, HTTPStatus.OK)

    def handle_create_product(self, data: ProductCreateDTO) -> dict:
        count_id: int = self.product_repo.get_count_id()
        code: str = CodeName.PRODUCT_CODE_NAME.value + str(count_id)
        is_data_entry: bool = False
        is_delete: bool = False
        product = Product(
            code=code,
            name=data.name,
            description=data.description,
            is_data_entry=is_data_entry,
            is_delete=is_delete,
            product_type_id=data.product_type_id,
            producer_id=data.producer_id,
        )
        self.commons.create(product)
        message = self.commons.get_message("create successful product")
        return self.commons.response_func_http(message, HTTPStatus.CREATED)
