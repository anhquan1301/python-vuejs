from http import HTTPStatus
from sqlalchemy.orm import scoped_session
import azure.functions as func
from auth.auth import Authencation
from dto.product.DataEntryDTO import DataEntryDTO
from dto.product.ProductCreateDTO import ProductCreateDTO

from service.ProductService import ProductService


class ProductController:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.product_service = ProductService(db=db)
        
    @Authencation.authenticate_and_authorize(["ROLE_ADMIN"])
    def get_product_list(self, req=func.HttpRequest) -> func.HttpResponse:
        value_select = {
            "name_search": req.params.get("name") or "",
            "product_type_id": req.params.get("productTypeId"),
            "producer_id": req.params.get("producerId"),
            "min_price": req.params.get("minPrice"),
            "max_price": req.params.get("maxPrice"),
            "page": req.params.get("page") or 0,
            "sort_type": req.params.get("sortType"),
        }

        response = self.product_service.get_product_list(value_select)
        return response

    def create_product(self, req=func.HttpRequest) -> func.HttpResponse:
        data = req.get_json()
        product_dto = ProductCreateDTO(**data)
        response = self.product_service.handle_create_product(product_dto)
        return response

    def create_product_capacity(self, req=func.HttpRequest) -> func.HttpResponse:
        data = req.get_json()
        product_capacity = DataEntryDTO(**data)
        response = self.product_service.handle_data_entry(product_capacity)
        return response
