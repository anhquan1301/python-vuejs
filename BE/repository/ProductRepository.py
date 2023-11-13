from sqlalchemy import case, func
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
    ):
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
                Product.code.label("product_code"),
                Product.name.label("product_name"),
                Product.description.label("description"),
                Color.hex_code.label("color_code"),
                Color.name.label("color_name"),
                Image.name.label("image_name"),
                sub_query.c.price_sale.label("price_sale"),
                ProductCapacity.price.label("price"),
                ProductCapacity.quantity.label("quantity"),
                Producer.name.label("producer_name"),
                ProductType.name.label("product_type_name"),
            )
            .select_from(Product)
            .join(sub_query, Product.id == sub_query.c.product_id)
            .join(ProductCapacity, ProductCapacity.product_id == Product.id)
            .join(ProductType, ProductType.id == Product.product_type_id)
            .join(Producer, Producer.id == Product.producer_id)
            .join(Color, Color.id == Product.color_id)
            .join(Image, Image.product_capacity_id == ProductCapacity.id)
            .filter(
                Product.name.like(f"%{name_search}%"),
                (
                    Product.product_type_id.is_(None)
                    | (Product.product_type_id == product_type_id)
                ),
                (Product.producer_id.is_(None) | (Product.producer_id == producer_id)),
                Product.is_delete.is_(False),
                Product.is_data_entry.is_(True),
                sub_query.c.price_sale >= min_price,
                sub_query.c.price_sale <= max_price,
            )
            .order_by(
                case(
                    (
                        sort_type == SortType.SORT_PRICE_DESC.value,
                        sub_query.c.price_sale * -1,
                    ),
                    (
                        sort_type == SortType.SORT_PRICE_ASC.value,
                        sub_query.c.price_sale,
                    ),
                    (
                        sort_type == SortType.SORT_NAME_DESC.value,
                        Product.name * -1,
                    ),
                    (
                        sort_type == SortType.SORT_NAME_ASC.value,
                        Product.name,
                    ),
                    else_=Product.id * -1,
                )
            )
            .limit(limit)
            .offset(offset)
        )
        self.db.commit()
        result = query.all()

        return result
