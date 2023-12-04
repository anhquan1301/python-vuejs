from enum import Enum


class AccessTokenExprie(Enum):
    MINUTE = 24 * 60 * 60


class ValueOfRole(Enum):
    ROLE_ADMIN = 1
    ROLE_EMPLOYEE = 2
    ROLE_CUSTOMER = 3


class SortType(Enum):
    SORT_PRICE_DESC = "1"
    SORT_PRICE_ASC = "2"
    SORT_NAME_DESC = "3"
    SORT_NAME_ASC = "4"


class LimitOfPage(Enum):
    LIMIT = 2


class CodeName(Enum):
    PRODUCT_CODE_NAME = "SP-"
    CUSTOMER_CODE_NAME = "KH-"

class ALGORITHM(Enum):
    ALGORITHM_VALUE = "HS256"
