from fastapi import APIRouter, Depends, status
import azure.functions as func
from auth.auth import Authencation
from dto.account.AccountLoginDTO import AccountDTO
from dto.account.RegistrationDataDTO import RegistrationDataDTO
from service.AuthService import AuthService
import json


class AuthController:
    def __init__(self, req) -> None:
        self.req = req
        self.auth_service = AuthService()
        self.authentica = Authencation()

    def login(self) -> func.HttpResponse:
        data = self.req.get_json()
        account_by_request = AccountDTO(
            username=data["username"], password=data["password"]
        )
        response = self.auth_service.handle_login(account_by_request)
        return response

    def register(self, req: func.HttpRequest) -> func.HttpResponse:
        data = req.get_json()
        registration_data = RegistrationDataDTO(
            email=data["email"], username=data["username"], password=["password"]
        )
        response = self.auth_service.handle_register(registration_data)
        return func.HttpResponse(json.dumps(response), status_code=200)
