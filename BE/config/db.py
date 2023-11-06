import importlib
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DB = "postgresql://postgres:123456@localhost:5432/dieucosmetics"

engine = create_engine(URL_DB)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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


# def update_database():
#     metadata = Base.metadata
#     metadata.create_all(engine, checkfirst=True)
