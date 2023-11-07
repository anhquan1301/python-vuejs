from dataclasses import dataclass
from datetime import timedelta
from fastapi import HTTPException, status
from auth.auth import Authencation
from common.Commons import Commons
from core.Enum import AccessTokenExprie, ValueOfRole
from dto.account.AccountLoginDTO import AccountDTO
from dto.account.RegistrationDataDTO import RegistrationDataDTO
from model.Account import Account
from model.AccountRoleAssociation import AccountRoleAssociation
from model.Role import Role


class AuthService:
    commons = Commons()

    def handle_login(self, account_by_request: AccountDTO) -> dict:
        authencation = Authencation()
        account = authencation.authenticate_user(
            account_by_request.username, account_by_request.password
        )
        if not account:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )

        account_role_accsociation = self.commons.get_model(
            AccountRoleAssociation, "account_id", account.id
        )
        if not account_role_accsociation:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="account role accsociation is not exist",
            )
        role_user = self.commons.get_all_models(
            Role, "id", account_role_accsociation.role_id
        )
        role_name = [role.name for role in role_user]
        if not role_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="role of user is not exist",
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
        return result

    def handle_register(self, data: RegistrationDataDTO) -> dict:
        is_exist_username = self.commons.check_exist(Account, "username", data.username)
        if is_exist_username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="username already exist"
            )
        is_exist_email = self.commons.check_exist(Account, "email", data.email)
        if is_exist_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="email already exist"
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
        return result
