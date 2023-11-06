from fastapi import FastAPI
import uvicorn
from config.db import create_database
from controller.AuthController import AuthController

app = FastAPI()
app.include_router(AuthController.auth_router)
create_database()


def start():
    uvicorn.run(app, host="0.0.0.0", port=8080)


# if __name__ == "__main__":
#     start()
