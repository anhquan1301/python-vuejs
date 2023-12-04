import datetime
from http import HTTPStatus
import json
from typing import Any, Type, get_type_hints
from passlib.context import CryptContext
import azure.functions as funct
from pydantic import BaseModel, ValidationError
from sqlalchemy.orm import scoped_session
from sqlalchemy import func


class Commons:
    def __init__(self, db: scoped_session) -> None:
        self.db = db
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_model(self, model, field, value):
        model = self.db.query(model).filter(getattr(model, field) == value).first()
        return model

    def get_all_models(self, model, field, value):
        models = self.db.query(model).filter(getattr(model, field) == value).all()
        return models

    def check_exist(self, model, field, value) -> bool:
        is_exist = bool(
            self.db.query(model).filter(getattr(model, field) == value).first()
        )
        return is_exist

    def create(self, model):
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model

    def create_all(self, models):
        self.db.add_all(models)
        self.db.commit()
        for model in models:
            self.db.refresh(model)
        return models

    def update(self, model, field, value, update_data: dict) -> None:
        instance = self.get_model(self, model, field, value)
        if instance:
            for key, value in update_data.items():
                setattr(instance, key, value)
            self.db.commit()
            self.db.refresh(instance)
            return instance
        return None

    def update_then_not_exist(self, model, update_data: dict):
        for key, value in update_data.items():
            setattr(model, key, value)
        self.db.commit()
        self.db.refresh(model)
        return model

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def response_func_http(
        self, data: dict, status_code: HTTPStatus
    ) -> funct.HttpResponse:
        def convert_dates(obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.strftime("%d-%m-%Y")
            return obj

        return funct.HttpResponse(
            status_code=status_code,
            body=json.dumps(data, default=convert_dates),
            mimetype="application/json",
        )

    def get_message_error(self, e: ValidationError) -> dict:
        return {"message": (e.errors()[0]["type"])}

    def get_error(self, message: str, http_status: HTTPStatus):
        return {"message": message, "http_status": http_status}

    def get_message(self, message: str):
        return {"message": message}

    def get_count_id(self, model) -> any:
        query = (
            self.db.query(func.count(model.id).label("count"))
            .select_from(model)
            .scalar()
        )
        return query
