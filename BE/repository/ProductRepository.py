from sqlalchemy import Numeric, and_, case, cast, func, or_
from sqlalchemy.orm import scoped_session
from core.Enum import LimitOfPage, SortType
from model.Color import Color
from model.Image import Image
from model.Producer import Producer
from model.Product import Product

from model.ProductCapacity import ProductCapacity
from model.ProductType import ProductType


class ProductRepository:
    def __init__(self, db: scoped_session) -> None:
        self.db = db

    def get_product_list(
        self,
        name_search: str,
        product_type_id: int,
        producer_id: int,
        min_price: int,
        max_price: int,
        page: int,
        sort_type: str,
    ) -> list:
        limit = LimitOfPage.LIMIT.value
        offset = page * limit
        sub_query = (
            self.db.query(
                ProductCapacity.product_id,
                func.min(ProductCapacity.price_sale).label("price_sale"),
            )
            .select_from(ProductCapacity)
            .group_by(ProductCapacity.product_id)
            .subquery()
        )
        query = (
            self.db.query(
                Product.id.label("product_id"),
                Product.code.label("product_code"),
                Product.name.label("product_name"),
                Image.name.label("image_name"),
                sub_query.c.price_sale.label("price_sale"),
                ProductCapacity.price.label("price"),
            )
            .select_from(Product)
            .join(sub_query, Product.id == sub_query.c.product_id)
            .join(ProductCapacity, ProductCapacity.product_id == Product.id)
            .join(ProductType, ProductType.id == Product.product_type_id)
            .join(Producer, Producer.id == Product.producer_id)
            .join(Color, Color.id == ProductCapacity.color_id)
            .join(
                Image,
                (Image.product_capacity_id == ProductCapacity.id)
                & (ProductCapacity.price_sale == sub_query.c.price_sale)
                & (Image.is_display == True),
            )
            .filter(
                Product.name.like(f"%{name_search}%"),
                or_(
                    and_(
                        (product_type_id is not None),
                        (Product.product_type_id == product_type_id),
                    ),
                    and_(
                        (product_type_id is None),
                        (Product.product_type_id == Product.product_type_id),
                    ),
                ),
                or_(
                    and_(
                        (producer_id is not None),
                        (Product.producer_id == producer_id),
                    ),
                    and_(
                        (producer_id is None),
                        (Product.producer_id == Product.producer_id),
                    ),
                ),
                Product.is_delete.is_(False),
                Product.is_data_entry.is_(True),
                sub_query.c.price_sale >= min_price,
                sub_query.c.price_sale <= max_price,
            )
            .order_by(
                case(
                    (
                        sort_type == SortType.SORT_PRICE_DESC.value,
                        cast(sub_query.c.price_sale, Numeric) * -1,
                    ),
                    (
                        sort_type == SortType.SORT_PRICE_ASC.value,
                        cast(sub_query.c.price_sale, Numeric),
                    ),
                    (
                        sort_type == SortType.SORT_NAME_DESC.value,
                        cast(Product.name, Numeric) * -1,
                    ),
                    (
                        sort_type == SortType.SORT_NAME_ASC.value,
                        cast(Product.name, Numeric),
                    ),
                    else_=cast(Product.id, Numeric) * -1,
                )
            )
            .limit(limit)
            .offset(offset)
        )
        result = query.all()
        return result


