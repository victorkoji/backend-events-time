from datetime import date
from pydantic import BaseModel, EmailStr


class LoginSchema(BaseModel):
    email: str
    password: str

class RefreshTokenInputSchema(BaseModel):
    refresh_token: str

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class RegisterInputSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    email: EmailStr
    cellphone: str
    password: str
