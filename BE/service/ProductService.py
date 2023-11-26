from http import HTTPStatus
from sqlalchemy.orm import scoped_session
from core.Enum import CodeName
from dto.product.DataEntryDTO import DataEntryDTO
from dto.product.ProductCreateDTO import ProductCreateDTO
from model.Image import Image
from model.Product import Product
from model.ProductCapacity import ProductCapacity

from repository.ProductRepository import ProductRepository
from common.Commons import Commons


class ProductService:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.product_repo = ProductRepository(db=self.db)
        self.commons = Commons(db=db)

    def get_product_list(self, value_search: dict) -> dict:
        result_product_list: list = self.product_repo.get_product_list(**value_search)
        response = self.commons.get_message("Retrieve data successfully")
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

    def handle_data_entry(self, data: DataEntryDTO):
        product = self.commons.get_model(Product, Product.id.name, data.product_id)
        if not product:
            error_mesage = self.commons.get_message("Product does not exist")
            raise Exception(error_mesage)
        data_entry_list: list = data.data_entry_list
        for element in data_entry_list:
            product_capacity = ProductCapacity(
                price=element.price,
                price_sale=element.price_sale,
                quantity=element.quantity,
                product_id=element.product_id,
                capacity_id=element.capacity_id,
                color_id=element.color_id,
            )
            product_capacity_new = self.commons.create(product_capacity)
            image_list: list = []
            product_capacity_id = product_capacity_new.id
            for item in element.image_list:
                image = Image(name=item.name, product_capacity_id=product_capacity_id)
                image_list.append(image)
            self.commons.create_all(image_list)
        product_update = {"is_data_entry": True}
        self.commons.update_then_not_exist(product, product_update)
        message = self.commons.get_message("data entry successful")
        return self.commons.response_func_http(message, HTTPStatus.CREATED)
