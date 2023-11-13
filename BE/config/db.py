import importlib
import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

log_file_path = os.path.join("log", "sql.log")

logging.basicConfig()

logging.basicConfig(filename=log_file_path, level=logging.INFO)

logging.getLogger("sqlalchemy.engine").setLevel(logging.ERROR)
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

URL_DB = "postgresql://postgres:123456@localhost:5432/dieucosmetics"

engine = create_engine(URL_DB)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()


def create_database():
    package_name = "model"
    directory_path = "D:\dieucosmetics\BE\model"
    files = [file for file in os.listdir(directory_path) if file.endswith(".py")]
    for file in files:
        if file != "BaseModel":
            module_name = f"{package_name}.{file[:-3]}"
            module = importlib.import_module(module_name)
            for name in dir(module):
                obj = getattr(module, name)
                if hasattr(obj, "__table__"):
                    obj.__table__.create(engine, checkfirst=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
