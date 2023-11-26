from sqlalchemy.orm import scoped_session


class CustomerService:
    def __init__(self, db: scoped_session) -> None:
        self.db = db

    def handle_get_customer_detail(self):
        pass
