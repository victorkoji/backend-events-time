from typing import Union
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from services.auth_service import AuthService
from schemas.auth_schema import LoginSchema, TokenSchema


auth_service = AuthService()
router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login", response_model=Union[TokenSchema, None])
def login(user: LoginSchema):
    try:
        token = auth_service.login(user.dict())
        return JSONResponse(content={'token': token})
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=None)
