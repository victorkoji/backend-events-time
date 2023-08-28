from typing import Optional
from datetime import date
from pydantic import BaseModel


class TokenFcmSchemaInput(BaseModel):
    token_fcm: str


class TokenFcmSchemaResponse(BaseModel):
    token_fcm: str


class UserCreateSchemaInput(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    email: str
    cellphone: str
    password: str
    token_fcm: Optional[float] = None


class UserSchemaResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: date
    email: str
    cellphone: str
    user_group_id: Optional[int] = None
