from typing import List
from pydantic import BaseModel
from schemas.product_schema import ProductMenuSchema


class ProductCategoryCreateSchema(BaseModel):
    name: str
    event_id: int


class ProductCategorySchema(BaseModel):
    id: int
    name: str
    event_id: int

class MenuSchema(BaseModel):
    id: int
    name: str
    products: List[ProductMenuSchema]
