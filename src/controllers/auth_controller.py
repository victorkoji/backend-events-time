from typing import Union
from fastapi import APIRouter, HTTPException, status, Request
from fastapi.responses import JSONResponse
from services.auth_service import AuthService
from services.user_service import UserService
from schemas.auth_schema import LoginSchema, TokenSchema
from schemas.user_schema import UserSchema


auth_service = AuthService()
user_service = UserService()

router_private = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

router_public = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router_public.post("/login", response_model=Union[TokenSchema, None])
def login(user: LoginSchema):
    try:
        token = auth_service.login(user.dict())
        return JSONResponse(content={'token': token})
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=None)


@router_private.get("/logged", response_model=UserSchema)
def logged(request: Request):
    try:
        user_token = request.state.user
        user = user_service.get(user_token['id'])
        return user.serialize()
    except:
        raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail=None)
