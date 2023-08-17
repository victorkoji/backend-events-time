import json

from typing import Any, Union
from pydantic import BaseModel, Json
from schemas.stand_schema import StandNameSchema
from schemas.product_file_schema import ProductFileSchema

class ProductCreateSchema(BaseModel):
    name: str
    price: float
    product_category_id: int
    stand_id: int
    custom_form_template: Json[Any] = None

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    custom_form_template: Json[Any]
    product_category_id: int
    product_file_id: Union[int, None]
    stand_id: int


class ProductMenuSchema(BaseModel):
    id: int
    name: str
    price: float
    stand: Union[StandNameSchema, None]
    product_file: Union[ProductFileSchema, None]
