from pydantic import BaseModel


class ProductCategoryCreateSchema(BaseModel):
    name: str


class ProductCategorySchema(BaseModel):
    id: int
    name: str
