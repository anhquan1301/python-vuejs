from http import HTTPStatus
from dotenv import load_dotenv
import os
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from common.Commons import Commons
from core.Enum import ValueOfRole
from model.Account import Account
import azure.functions as func
from sqlalchemy.orm import scoped_session


class Authencation:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.error_message: dict
        self.commons = Commons(db=self.db)
        self.dotenv = load_dotenv()
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ALGORITHM = "HS256"
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def create_access_token(self, data: dict, expires_delta: timedelta) -> jwt:
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def authenticate_user(self, username: str, password: str):
        account = self.commons.get_model(Account, "username", username)
        if not account:
            return False
        if not self.commons.verify_password(password, account.password):
            return False
        return account

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return payload
        except JWTError:
            self.error_message = self.commons.get_error(
                "Could not validate credentials", HTTPStatus.FORBIDDEN
            )
            raise Exception(self.error_message)

    def get_token(self, req: func.HttpRequest) -> str:
        token = req.headers.get("Authorization")
        if token and token.startswith("Bearer "):
            return token[len("Bearer ") :]
        return ""

    def get_current_user(self, req: func.HttpRequest):
        token = self.get_token(req)
        if token is None:
            self.error_message = self.commons.get_error(
                "Invalid token", HTTPStatus.UNAUTHORIZED
            )
            raise Exception(self.error_message)
        user_info = self.verify_token(token)
        return user_info

    def check_admin_role(self, user_info: dict = Depends(get_current_user)) -> bool:
        if ValueOfRole.ROLE_ADMIN.name not in user_info:
            self.error_message = self.commons.get_error(
                "Permission denied", HTTPStatus.FORBIDDEN
            )
            raise Exception(self.error_message)
        return True

    def check_admin_or_employee_role(
        self,
        user_info: dict = Depends(get_current_user),
    ) -> bool:
        allowed_roles = {ValueOfRole.ROLE_ADMIN.name, ValueOfRole.ROLE_EMPLOYEE.name}
        if not any(role in allowed_roles for role in user_info["role"]):
            self.error_message = self.commons.get_error(
                "Permission denied", HTTPStatus.FORBIDDEN
            )
            raise Exception(self.error_message)
        return True

    def check_admin_or_customer_role(
        self,
        user_info: dict = Depends(get_current_user),
    ) -> bool:
        allowed_roles = {ValueOfRole.ROLE_ADMIN.name, ValueOfRole.ROLE_CUSTOMER.name}
        if not any(role in allowed_roles for role in user_info["role"]):
            self.error_message = self.commons.get_error(
                "Permission denied", HTTPStatus.FORBIDDEN
            )
            raise Exception(self.error_message)
        return True

    def check_login_status(self, token: str = Depends(get_current_user)) -> bool:
        if not token:
            self.error_message = self.commons.get_error(
                "You need to log in first", HTTPStatus.UNAUTHORIZED
            )
            raise Exception(self.error_message)
        return True
