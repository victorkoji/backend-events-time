from pydantic import BaseModel


class ProductCreateSchema(BaseModel):
    name: str
    price: float
    product_category_id: int


class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    product_category_id: int
