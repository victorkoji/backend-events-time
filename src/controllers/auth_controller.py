from fastapi import APIRouter, HTTPException
from services.auth_service import AuthService
from schemas.auth_schema import LoginSchema, TokenSchema
from fastapi.responses import JSONResponse
from typing import Union


auth_service = AuthService()
router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login", response_model=Union[TokenSchema, None])
def login(user: LoginSchema):
    token = auth_service.login(user.dict())
    return JSONResponse(content={'token': token}, status_code=200)
