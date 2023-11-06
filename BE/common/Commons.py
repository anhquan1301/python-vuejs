from config.db import SessionLocal
from passlib.context import CryptContext


class Commons:
    db = SessionLocal()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_model(self, model, field, value):
        model = self.db.query(model).filter(getattr(model, field) == value).first()
        return model

    def get_all_models(self, model, field, value):
        models = self.db.query(model).filter(getattr(model, field) == value).all()
        return models

    def check_exist(self, model, field, value):
        is_exist = bool(
            self.db.query(model).filter(getattr(model, field) == value).first()
        )
        return is_exist

    def create(self, model):
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model

    def update(self, model, field, value, update_data: dict):
        instance = self.check_exist(self, model, field, value)
        if not instance:
            for key, value in update_data.items():
                setattr(instance, key, value)
            self.db.commit()
            self.db.refresh(instance)
            return instance
        return None

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)
