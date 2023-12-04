from http import HTTPStatus
from sqlalchemy.orm import scoped_session

from common.Commons import Commons
from core.Enum import CodeName
from dto.user.CustomerCreateDTO import CustomerCreateDTO
from model.Account import Account
from model.Customer import Customer
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
            "avatar": customer.avatar,
        }
        response["data"] = data_response
        return self.commons.response_func_http(response, HTTPStatus.OK)

    def handle_create_customer(self, data: CustomerCreateDTO, username: str):
        count_id = self.commons.get_count_id(Customer)
        code: str = CodeName.CUSTOMER_CODE_NAME.value + str(count_id)
        customer_model = Customer(**data.dict())
        customer_model.code = code
        customer_model.point = 0
        account = self.commons.get_model(Account, Account.username.name, username)
        customer_model.account_id = account.id
        self.commons.create(customer_model)
        message = self.commons.get_message("Successfully added new customers")
        return self.commons.response_func_http(message, HTTPStatus.CREATED)
