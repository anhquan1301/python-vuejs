from http import HTTPStatus
from sqlalchemy.orm import scoped_session

from common.Commons import Commons
from model.Account import Account
from repository.CustomerRepository import CustomerRepository


class CustomerService:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.commons = Commons(db=self.db)
        self.customer_repo = CustomerRepository(db=db)

    def handle_get_customer_detail(self, username: str):
        customer = self.customer_repo.get_customer_detail(username)
        if customer is None:
            error_message = self.commons.get_error(
                "User does not exist", HTTPStatus.BAD_REQUEST
            )
            raise Exception(error_message)
        response = self.commons.get_message("Retrieve data successfully")
        data_response = {
            "id": customer.id,
            "code": customer.code,
            "name": customer.name,
            "gender": "Nam" if customer.gender is True else "Nữ",
            "numberPhone": customer.number_phone,
            "address": customer.address,
            "dateOfBirth": customer.date_of_birth,
            "point": customer.point,
        }
        response["data"] = data_response
        return self.commons.response_func_http(response, HTTPStatus.OK)
