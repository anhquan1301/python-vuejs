from http import HTTPStatus
from sqlalchemy.orm import scoped_session

from repository.ProductRepository import ProductRepository
from common.Commons import Commons


class ProductService:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.product_repo = ProductRepository(db=self.db)
        self.commons = Commons(db=db)

    def get_product_list(self, value_search: dict):
        result = self.product_repo.get_product_list(**value_search)
        if len(result) > 0:
            return self.commons.response_func_http({"ms": "ok"}, HTTPStatus.OK)
        return self.commons.response_func_http({"ms": "err"}, HTTPStatus.OK)
