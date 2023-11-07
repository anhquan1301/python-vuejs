from fastapi import APIRouter, Depends, status
import azure.functions as func
from auth.auth import Authencation
from dto.account.AccountLoginDTO import AccountDTO
from dto.account.RegistrationDataDTO import RegistrationDataDTO
from service.AuthService import AuthService


class AuthController:
    auth_service = AuthService()
    authentica = Authencation()

    def login(self, req: func.HttpRequest) -> func.HttpResponse:
        data = req.get_json()
        account_by_request: AccountDTO = data
        response = AuthController.auth_service.handle_login(account_by_request)
        return func.HttpResponse(response, status_code=200)

    def register(self, req: func.HttpRequest) -> func.HttpResponse:
        registration_data = req.get_body()
        response = AuthController.auth_service.handle_register(registration_data)
        return response

    def create_product(self, req: func.HttpRequest) -> func.HttpResponse:
        return func.HttpResponse("Product created successfully.", status_code=200)

    def update_product(self, req: func.HttpRequest) -> func.HttpResponse:
        return func.HttpResponse("Product update successfully.", status_code=200)
