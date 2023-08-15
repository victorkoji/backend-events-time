from pydantic import BaseModel


class StandCreateSchema(BaseModel):
    name: str
    is_cashier: bool
    stand_category_id: int
    event_id: int


class StandSchema(BaseModel):
    id: int
    name: str
    is_cashier: bool
    stand_category_id: int
    event_id: int

class StandNameCashierSchema(BaseModel):
    id: int
    name: str
    is_cashier: bool

class StandNameSchema(BaseModel):
    id: int
    name: str
