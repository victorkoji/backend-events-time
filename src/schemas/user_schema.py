from pydantic import BaseModel
from datetime import date


class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    email: str
    cellphone: str
    password: str
    password: str


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: date
    email: str
    cellphone: str
