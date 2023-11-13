from http import HTTPStatus
import azure.functions as func
from pydantic import ValidationError
from auth.auth import Authencation
from dto.account.AccountLoginDTO import AccountDTO
from dto.account.ChangePasswordDTO import ChangePasswordDTO
from dto.account.RegistrationDataDTO import RegistrationDataDTO
from service.AuthService import AuthService
from common.Commons import Commons

from sqlalchemy.orm import scoped_session


class AuthController:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.auth_service = AuthService(db=self.db)
        self.authenticate = Authencation(db=self.db)
        self.commons = Commons(db=self.db)

    def login(self, req=func.HttpRequest) -> func.HttpResponse:
        try:
            data = req.get_json()
            account_by_request = AccountDTO(**data)
            response = self.auth_service.handle_login(account_by_request)
            return response
        except ValidationError as e:
            error_message = self.commons.get_message_error(e)
            return self.commons.response_func_http(
                error_message, HTTPStatus.BAD_REQUEST
            )

    def register(self, req=func.HttpRequest) -> func.HttpResponse:
        try:
            data = req.get_json()
            registration_data = RegistrationDataDTO(**data)
            response = self.auth_service.handle_register(registration_data)
            return response
        except ValidationError as e:
            error_message = self.commons.get_message_error(e)
            return self.commons.response_func_http(
                error_message, HTTPStatus.BAD_REQUEST
            )

    def change_password(self, req=func.HttpRequest) -> func.HttpResponse:
        try:
            data = req.get_json()
            change_password_data = ChangePasswordDTO(**data)
            user = self.authenticate.get_current_user(req=req)
            response = self.auth_service.handle_change_password(
                change_password_data, username=user["username"]
            )
            return response
        except ValidationError as e:
            error_message = self.commons.get_message_error(e)
            return self.commons.response_func_http(
                error_message, HTTPStatus.BAD_REQUEST
            )
    