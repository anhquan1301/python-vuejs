from datetime import timedelta
from auth.auth import Authencation
from common.Commons import Commons
from core.Enum import AccessTokenExprie, ValueOfRole
from dto.account.AccountLoginDTO import AccountDTO
from dto.account.ChangePasswordDTO import ChangePasswordDTO
from dto.account.RegistrationDataDTO import RegistrationDataDTO
from model.Account import Account
from model.AccountRoleAssociation import AccountRoleAssociation
from model.Role import Role
import azure.functions as func
from http import HTTPStatus
from sqlalchemy.orm import scoped_session


class AuthService:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.error_message: dict
        self.commons = Commons(db=self.db)
        self.authencation = Authencation(db=self.db)

    def handle_login(self, account_by_request: AccountDTO) -> func.HttpResponse:
        account = self.authencation.authenticate_user(
            account_by_request.username, account_by_request.password
        )
        if not account:
            self.error_message = self.commons.get_error(
                "Invalid username or password", HTTPStatus.UNAUTHORIZED
            )
            raise Exception(self.error_message)
        account_role_accsociation = self.commons.get_model(
            AccountRoleAssociation, "account_id", account.id
        )
        if not account_role_accsociation:
            self.error_message = self.commons.get_error(
                "account role accsociation is not exist", HTTPStatus.UNAUTHORIZED
            )
            raise Exception(self.error_message)
        role_user = self.commons.get_all_models(
            Role, "id", account_role_accsociation.role_id
        )
        role_name = [role.name for role in role_user]
        if not role_user:
            self.error_message = self.commons.get_error(
                "role of user is not exist", HTTPStatus.UNAUTHORIZED
            )
            raise Exception(self.error_message)
        access_token_expires = timedelta(minutes=AccessTokenExprie.MINUTE.value)
        data = {"username": account_by_request.username, "role": role_name}
        access_token = self.authencation.create_access_token(
            data,
            expires_delta=access_token_expires,
        )
        result = {
            "username": account.username,
            "role": role_name,
            "accessToken": access_token,
            "tokenType": "bearer",
        }
        return self.commons.response_func_http(result, HTTPStatus.OK)

    def handle_register(self, data: RegistrationDataDTO) -> dict:
        is_exist_username = self.commons.check_exist(Account, "username", data.username)
        if is_exist_username:
            self.error_message = self.commons.get_error(
                "username already exist", HTTPStatus.BAD_REQUEST
            )
            raise Exception(self.error_message)
        is_exist_email = self.commons.check_exist(Account, "email", data.email)
        if is_exist_email:
            self.error_message = self.commons.get_error(
                "email already exist", HTTPStatus.BAD_REQUEST
            )
            raise Exception(self.error_message)
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
        result = self.commons.get_message("registration successful")
        return self.commons.response_func_http(result, HTTPStatus.CREATED)

    def handle_change_password(self, data: ChangePasswordDTO, username: str):
        hashed_new_password = self.commons.get_password_hash(data.new_password)
        is_exist_user = self.commons.get_model(Account, "username", username)
        if not is_exist_user:
            self.error_message = self.commons.get_error(
                "The user does not exist.", HTTPStatus.BAD_REQUEST
            )
            raise Exception(self.error_message)
        if not self.commons.verify_password(data.password, is_exist_user.password):
            self.error_message = self.commons.get_error(
                "The current password is incorrect.", HTTPStatus.BAD_REQUEST
            )
            raise Exception(self.error_message)
        if self.commons.verify_password(data.new_password, is_exist_user.password):
            self.error_message = self.commons.get_error(
                "The current password is identical to the old password.",
                HTTPStatus.BAD_REQUEST,
            )
            raise Exception(self.error_message)
        if data.new_password != data.confirm_password:
            self.error_message = self.commons.get_error(
                "The confirmation password does not match.", HTTPStatus.BAD_REQUEST
            )
            raise Exception(self.error_message)
        value = {"password": hashed_new_password}
        self.commons.update_then_not_exist(is_exist_user, value)
        result = self.commons.get_message("The password has been successfully changed.")
        return self.commons.response_func_http(result, HTTPStatus.OK)
