from http import HTTPStatus
from sqlalchemy.orm import scoped_session
import azure.functions as func

from service.ProductService import ProductService


class ProductController:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.product_service = ProductService(db=db)

    def get_product_list(self, req=func.HttpRequest) -> func.HttpResponse:
        value_select = {
            "name_search": req.params.get("name") or "",
            "product_type_id": req.params.get("productTypeId"),
            "producer_id": req.params.get("producerId"),
            "min_price": req.params.get("minPrice"),
            "max_price": req.params.get("maxPrice"),
            "page": req.params.get("page"),
            "sort_type": req.params.get("sortType"),
        }
        try:
            response = self.product_service.get_product_list(value_select)
            self.db.commit()
            return response
        except Exception as e:
            self.db.rollback()
            return func.HttpResponse(
                "Internal Server Error", status_code=HTTPStatus.INTERNAL_SERVER_ERROR
            )
        finally:
            self.db.close()
