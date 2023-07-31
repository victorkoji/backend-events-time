from typing import List, Union
from fastapi import APIRouter, HTTPException, Response, status
from services.user_service import UserService
from schemas.user_schema import UserCreateSchema, UserSchema


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
        return users.serialize()
    except Exception as ex:
        raise handle_exception(ex)


@router.get('/{user_id}', response_model=UserSchema)
def get_user(user_id: int):
    try:
        user = user_service.get(user_id)
        return user.serialize()
    except Exception as ex:
        raise handle_exception(ex)


@router.post("/", response_model=Union[UserSchema, None], status_code=status.HTTP_201_CREATED)
def add_user(user: UserCreateSchema):
    try:
        if user_service.get_by_email(user.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The user with this email already exists in the system.",
            )

        user = user_service.add(user.dict())

        return user.serialize()

    except Exception as ex:
        raise handle_exception(ex)


@router.put("/", response_model=Union[UserSchema, None])
def update_user(user: UserSchema):
    try:
        user = user_service.update(user.dict())
        return user.serialize()

    except Exception as ex:
        raise handle_exception(ex)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_user(user_id: int):
    try:
        user_service.delete(user_id)
    except Exception as ex:
        raise handle_exception(ex)


def handle_exception(ex):
    message_error = str(ex)
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return HTTPException(status_code=status_code, detail=message_error)
