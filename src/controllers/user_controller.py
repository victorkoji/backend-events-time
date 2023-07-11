from fastapi import APIRouter, HTTPException
from services.user_service import UserService
from schemas.user_schema import UserCreateSchema, UserSchema
from fastapi.responses import JSONResponse
from typing import List, Union
from exceptions.custom_exception import DatabaseError


user_service = UserService()
router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get('/', response_model=List[UserSchema])
def get_all_items():
    try:
        users = user_service.get()
        return JSONResponse(content=users.serialize(), status_code=200)
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)


@router.get('/{user_id}', response_model=UserSchema)
def get_product(user_id: int):
    try:
        product = user_service.get(user_id)
        return JSONResponse(content=product.serialize(), status_code=200)
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)


@router.post("/", response_model=Union[UserSchema, None])
def add_user(user: UserCreateSchema):
    try:
        if user_service.get_by_email(user.email):
            raise HTTPException(
                status_code=400,
                detail="The user with this email already exists in the system.",
            )

        user_service.add(user.dict())
        return JSONResponse(content={'message': 'User added successfully'}, status_code=201)

    except DatabaseError as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)


@router.delete("/{user_id}")
def delete_user(user_id: int):
    try:
        if user_service.delete(user_id):
            return JSONResponse(content={'message': 'User deleted successfully'}, status_code=200)
        else:
            return JSONResponse(content={'message': 'User not found'}, status_code=404)
    except DatabaseError as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)
