from datetime import date, datetime
from typing import Union, List
from pydantic import BaseModel
from schemas.stand_schema import StandNameCashierSchema


class EventCreateSchema(BaseModel):
    name: str
    programmed_date_initial: date
    programmed_date_final: date
    address: str
    is_public: bool


class EventSchema(BaseModel):
    id: int
    name: str
    programmed_date_initial: Union[date, datetime]
    programmed_date_final: Union[date, datetime]
    address: str
    is_public: bool


class EventByUserSchema(BaseModel):
    id: int
    name: str
    programmed_date_initial: Union[date, datetime]
    programmed_date_final: Union[date, datetime]
    is_public: bool
    stands: List[StandNameCashierSchema]
