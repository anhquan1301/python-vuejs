from http import HTTPStatus
import os
import azure.functions as func
from jose import JWTError, jwt
from typing import List
from core.Enum import ALGORITHM


class Authorization:
    ALGORITHM = ALGORITHM.ALGORITHM_VALUE.value
    SECRET_KEY = os.getenv("SECRET_KEY")

    def verify_token(token: str):
        try:
            payload = jwt.decode(
                token, Authorization.SECRET_KEY, algorithms=[Authorization.ALGORITHM]
            )
            return payload
        except JWTError:
            error_message = {
                "message": "Could not validate credentials",
                "http_status": HTTPStatus.FORBIDDEN,
            }
            raise Exception(error_message)

    def get_token(token: str) -> str:
        if token and token.startswith("Bearer "):
            return token[len("Bearer ") :]
        return ""

    def get_current_user(req: func.HttpRequest):
        data = req.headers.get("Authorization")
        token = Authorization.get_token(data)
        if token is None:
            error_message = {
                "message": "Invalid token",
                "http_status": HTTPStatus.UNAUTHORIZED,
            }
            raise Exception(error_message)
        user_info = Authorization.verify_token(token)
        return user_info

    def has_required_roles(user_info, allowed_roles: List[str]) -> bool:
        user_roles = user_info.get("role", [])
        return any(role in user_roles for role in allowed_roles)

    def authenticate_and_authorize(allowed_roles: List[str]):
        def decorator(function):
            def wrapper(req: func.HttpRequest = func.HttpRequest, *args, **kwargs):
                data = args[0].headers.get("Authorization")
                token = Authorization.get_token(data)
                user_info = Authorization.verify_token(token)
                if not Authorization.has_required_roles(user_info, allowed_roles):
                    error_message = {
                        "message": "Permission denied",
                        "http_status": HTTPStatus.FORBIDDEN,
                    }
                    raise Exception(error_message)
                return function(req, *args, **kwargs)

            return wrapper

        return decorator
