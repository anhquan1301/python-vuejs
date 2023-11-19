from fastapi import FastAPI
import uvicorn
from config.db import SessionLocal, create_database
from controller.AuthController import AuthController

app = FastAPI()
create_database()
db = SessionLocal()
db.rollback()

def start():
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    start()
