from dataclasses import dataclass
from datetime import timedelta
import json
from auth.auth import Authencation
from common.Commons import Commons
from core.Enum import AccessTokenExprie, ValueOfRole
from dto.account.AccountLoginDTO import AccountDTO
from dto.account.RegistrationDataDTO import RegistrationDataDTO
from model.Account import Account
from model.AccountRoleAssociation import AccountRoleAssociation
from model.Role import Role
import azure.functions as func
from http import HTTPStatus


class AuthService:
    def __init__(self) -> None:
        self.error_message: dict = {}
        self.commons = Commons()

    def handle_login(self, account_by_request: AccountDTO) -> dict:
        authencation = Authencation()
        account = authencation.authenticate_user(
            account_by_request.username, account_by_request.password
        )
        if not account:
            self.error_message = {"message": "Invalid username or password"}
            return func.HttpResponse(
                json.dumps(self.error_message), status_code=HTTPStatus.UNAUTHORIZED
            )

        account_role_accsociation = self.commons.get_model(
            AccountRoleAssociation, "account_id", account.id
        )
        if not account_role_accsociation:
            self.error_message = {"message": "account role accsociation is not exist"}
            return func.HttpResponse(
                json.dumps(self.error_message), status_code=HTTPStatus.UNAUTHORIZED
            )

        role_user = self.commons.get_all_models(
            Role, "id", account_role_accsociation.role_id
        )
        role_name = [role.name for role in role_user]
        if not role_user:
            self.error_message = {"message": "role of user is not exist"}
            return func.HttpResponse(
                json.dumps(self.error_message), status_code=HTTPStatus.UNAUTHORIZED
            )
        access_token_expires = timedelta(minutes=AccessTokenExprie.MINUTE.value)
        data = {"username": account_by_request.username, "role": role_name}
        access_token = authencation.create_access_token(
            data,
            expires_delta=access_token_expires,
        )
        result = {
            "username": account.username,
            "role": role_name,
            "access_token": access_token,
            "token_type": "bearer",
        }
        return func.HttpResponse(json.dumps(result), status_code=HTTPStatus.OK)

    def handle_register(self, data: RegistrationDataDTO) -> dict:
        is_exist_username = self.commons.check_exist(Account, "username", data.username)
        if is_exist_username:
            self.error_message = {"message": "username already exist"}
            return func.HttpResponse(
                json.dumps(self.error_message), status_code=HTTPStatus.BAD_REQUEST
            )
        is_exist_email = self.commons.check_exist(Account, "email", data.email)
        if is_exist_email:
            self.error_message = {"message": "email already exist"}
            return func.HttpResponse(
                json.dumps(self.error_message), status_code=HTTPStatus.BAD_REQUEST
            )
        hashed_password = self.commons.get_password_hash(data.password)
        new_account = Account(
            email=data.email,
            username=data.username,
            password=hashed_password,
        )

        account_created = self.commons.create(new_account)
        account_id = account_created.id
        account_role_association = AccountRoleAssociation(
            account_id=account_id, role_id=ValueOfRole.ROLE_CUSTOMER.value
        )
        self.commons.create(account_role_association)
        result = {"message": "registration successful"}
        return func.HttpResponse(json.dumps(result), status_code=HTTPStatus.CREATED)
