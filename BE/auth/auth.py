from http import HTTPStatus
from typing import List
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
from azure.functions import HttpRequest, HttpResponse
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

    
    def authenticate_and_authorize(allowed_roles: List[str]):
        def decorator(func):
            def wrapper(self, req=HttpRequest, *args, **kwargs):
                token = req.headers.get("Authorization")
                user_info = self.get_current_user(token)

                if not self.has_required_roles(user_info, allowed_roles):
                    self.error_message = self.commons.get_error(
                        "Permission denied", HTTPStatus.FORBIDDEN
                    )
                    raise Exception(self.error_message)

                return func(self, req, *args, **kwargs)

            return wrapper

        return decorator

    def has_required_roles(user_info, allowed_roles: List[str]) -> bool:
        user_roles = user_info.get("roles", [])
        return any(role in user_roles for role in allowed_roles)
