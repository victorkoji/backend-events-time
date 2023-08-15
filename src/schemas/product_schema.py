from typing import Any, Union
from pydantic import BaseModel, Json
from schemas.stand_schema import StandNameCashierSchema, StandNameSchema


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
    stand: Union[StandNameCashierSchema, None]

class ProductMenuSchema(BaseModel):
    id: int
    name: str
    price: float
    stand: Union[StandNameSchema, None]
