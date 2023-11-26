from sqlalchemy.orm import scoped_session

from service.CustomerService import CustomerService


class CustomerController:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.customer_service = CustomerService(db=self.db)

    def get_customer_detail(self):
        pass
