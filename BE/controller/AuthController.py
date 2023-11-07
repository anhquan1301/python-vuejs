from fastapi import APIRouter, Depends, status

from auth.auth import Authencation
from dto.account.AccountLoginDTO import AccountDTO
from dto.account.RegistrationDataDTO import RegistrationDataDTO
from service.AuthService import AuthService


class AuthController:
    #      {
    #   "scriptFile": "if_b40_001_controller.py",
    #   "bindings": [
    #     {
    #       "authLevel": "function",
    #       "type": "httpTrigger",
    #       "direction": "in",
    #       "name": "req",
    #       "methods": [
    #         "post"
    #       ],
    #       "route": "if-b40-001/{*route}"
    #     },
    #     {
    #       "type": "http",
    #       "direction": "out",
    #       "name": "$return"
    #     }
    #   ]
    # }

    auth_router = APIRouter()
    auth_service = AuthService()
    authentica = Authencation()

    @auth_router.post("/login", status_code=status.HTTP_200_OK)
    async def login(account_by_request: AccountDTO):
        response = AuthController.auth_service.handle_login(account_by_request)
        return response

    @auth_router.post("/register", status_code=status.HTTP_201_CREATED)
    async def register(registration_data: RegistrationDataDTO):
        response = AuthController.auth_service.handle_register(registration_data)
        return response

    @auth_router.get("/test", dependencies=[Depends(authentica.check_admin_role)])
    async def register():
        return "ok"
