from http import HTTPStatus
from sqlalchemy.orm import scoped_session
import azure.functions as func
from auth.auth import Authentication
from dto.product.DataEntryDTO import DataEntryDTO
from dto.product.ProductCreateDTO import ProductCreateDTO
from azure.functions import HttpRequest, HttpResponse
from service.ProductService import ProductService
from typing import List
from common.Commons import Commons
def authenticate_and_authorize(allowed_roles: List[str]):
    def decorator(function):
        def wrapper(req: func.HttpRequest = func.HttpRequest, *args, **kwargs):
            token = req.headers.get("Authorization")
            user_info = Authentication.get_current_user(token)
            if not Authentication.has_required_roles(user_info, allowed_roles):
                error_message = Commons.get_error(
                    "Permission denied", HTTPStatus.FORBIDDEN
                )
                raise Exception(error_message)
            return function(req, *args, **kwargs)

        return wrapper

    return decorator


class ProductController:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.product_service = ProductService(db=db)
        self.auth_instance = Authentication(db=db)

    @authenticate_and_authorize(allowed_roles=["ROLE_ADMIN"])
    def get_product_list(
        self, req: func.HttpRequest = func.HttpRequest
    ) -> func.HttpResponse:
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

    def create_product(
        self, req: func.HttpRequest = func.HttpRequest
    ) -> func.HttpResponse:
        data = req.get_json()
        product_dto = ProductCreateDTO(**data)
        response = self.product_service.handle_create_product(product_dto)
        return response

    def create_product_capacity(
        self, req: func.HttpRequest = func.HttpRequest
    ) -> func.HttpResponse:
        data = req.get_json()
        product_capacity = DataEntryDTO(**data)
        response = self.product_service.handle_data_entry(product_capacity)
        return response
