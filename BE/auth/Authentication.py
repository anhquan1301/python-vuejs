from dotenv import load_dotenv
import os
from jose import jwt
from datetime import datetime, timedelta
from common.Commons import Commons
from core.Enum import ALGORITHM
from model.Account import Account
from sqlalchemy.orm import scoped_session


class Authentication:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.error_message: dict
        self.commons = Commons(db=self.db)
        self.dotenv = load_dotenv()
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ALGORITHM = ALGORITHM.ALGORITHM_VALUE.value

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
