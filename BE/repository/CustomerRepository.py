from sqlalchemy.orm import scoped_session
from model.Account import Account

from model.Customer import Customer


class CustomerRepository:
    def __init__(self, db: scoped_session) -> None:
        self.db = db

    def get_customer_detail(self, username: str):
        query = (
            self.db.query(Customer).join(Account, Account.username == username).first()
        )
        return query
