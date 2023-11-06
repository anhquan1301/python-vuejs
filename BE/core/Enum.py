from enum import Enum


class AccessTokenExprie(Enum):
    MINUTE = 24 * 60 * 60


class ValueOfRole(Enum):
    ROLE_ADMIN = 1
    ROLE_EMPLOYEE = 2
    ROLE_CUSTOMER = 3


class NameOfRole(Enum):
    ADMIN = "ROLE_ADMIN"
    EMPLOYEE = "ROLE_EMPLOYEE"
    CUSTOMER = "ROLE_CUSTOMER"
