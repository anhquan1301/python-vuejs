from typing import Optional
from dotenv import load_dotenv
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from common.Commons import Commons
from core.Enum import NameOfRole
from model.Account import Account


class Authencation:
    commons = Commons()
    load_dotenv()
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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
            print(payload.get("role"))
            return payload.get("role")
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )

    async def get_current_user(self, token: Optional[str] = Depends(oauth2_scheme)):
        if token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )
        user_info = self.verify_token(token)
        return user_info

    async def check_admin_role(user_info: dict = Depends(get_current_user)) -> bool:
        if NameOfRole.ADMIN.value not in user_info:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied",
            )
        return True

    async def check_admin_or_employee_role(
        user_info: dict = Depends(get_current_user),
    ) -> bool:
        allowed_roles = {NameOfRole.ADMIN.value, NameOfRole.EMPLOYEE.value}
        if not any(role in allowed_roles for role in user_info["role"]):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied",
            )
        return True

    async def check_admin_or_customer_role(
        user_info: dict = Depends(get_current_user),
    ) -> bool:
        allowed_roles = {NameOfRole.ADMIN.value, NameOfRole.CUSTOMER.value}
        if not any(role in allowed_roles for role in user_info["role"]):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied",
            )
        return True

    async def check_login_status(token: str = Depends(get_current_user)) -> bool:
        if not token:
            raise HTTPException(status_code=401, detail="You need to log in first")
        return True
