from pydantic import BaseModel, Json
from typing import Any, Optional


class ProductCreateSchema(BaseModel):
    name: str
    price: float
    product_category_id: int
    custom_form_template: Json[Any]


class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    product_category_id: int
    custom_form_template: Json[Any]
