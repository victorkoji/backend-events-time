from typing import Union
from fastapi import APIRouter, HTTPException, status, Request, Response
from exceptions.auth_exception import UnathorizedError
from exceptions.user_exception import EmailAlreadyExistError
from exceptions.general_exception import DatabaseError
from services.auth_service import AuthService
from services.user_service import UserService
from schemas.auth_schema import LoginSchema, TokenSchema, RegisterInputSchema, RefreshTokenInputSchema
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
        return auth_service.login(user.dict())
    except UnathorizedError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=None)
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ex))


@router_public.post("/register")
def register(user: RegisterInputSchema):
    try:
        auth_service.register(user.dict())
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except EmailAlreadyExistError as ex:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=ex.message)
    except DatabaseError as ex:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=ex.message)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=None)


@router_public.post("/refresh-token", response_model=Union[TokenSchema, None])
async def refresh_token(refresh_token_input: RefreshTokenInputSchema):
    try:
        return auth_service.refresh_token(refresh_token_input.refresh_token)
    except UnathorizedError as ex:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=ex.message)
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ex))

@router_private.get("/logged", response_model=UserSchema)
def logged(request: Request):
    try:
        user_token = request.state.user
        user = user_service.get(user_token['id'])
        return user.serialize()
    except:
        raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail=None)
