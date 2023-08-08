from datetime import date
from pydantic import BaseModel, EmailStr


class LoginSchema(BaseModel):
    email: str
    password: str


class TokenSchema(BaseModel):
    token: str

class RegisterInputSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    email: EmailStr
    cellphone: str
    password: str
