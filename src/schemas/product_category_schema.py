from pydantic import BaseModel


class ProductCategoryCreateSchema(BaseModel):
    name: str
    event_id: int


class ProductCategorySchema(BaseModel):
    id: int
    name: str
    event_id: int
