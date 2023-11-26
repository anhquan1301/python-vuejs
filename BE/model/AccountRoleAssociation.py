from sqlalchemy import Column, Integer

from model.BaseModel import BaseModel


class AccountRoleAssociation(BaseModel):
    __tablename__ = "account_role_association"
    account_id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer)
