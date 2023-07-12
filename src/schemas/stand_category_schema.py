from pydantic import BaseModel


class StandCategoryCreateSchema(BaseModel):
    name: str
    event_id: int


class StandCategorySchema(BaseModel):
    id: int
    name: str
    event_id: int
