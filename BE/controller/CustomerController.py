from sqlalchemy.orm import scoped_session
import azure.functions as func
from auth.Authorization import Authorization
from service.CustomerService import CustomerService


class CustomerController:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.customer_service = CustomerService(db=self.db)

    def get_customer_detail(
        self, req: func.HttpRequest = func.HttpRequest
    ) -> func.HttpResponse:
        user = Authorization.get_current_user(req=req)
        username = user["username"]
        response = self.customer_service.handle_get_customer_detail(username)
        return response
