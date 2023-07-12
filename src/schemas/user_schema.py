from pydantic import BaseModel
from datetime import date
from typing import Optional


class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    email: str
    cellphone: str
    password: str
    token_fcm: Optional[float] = None


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: date
    email: str
    cellphone: str
