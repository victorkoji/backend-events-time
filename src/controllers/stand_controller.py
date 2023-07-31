from typing import List
from fastapi import APIRouter, Response, status, HTTPException
from fastapi.responses import JSONResponse
from services.stand_service import StandService
from schemas.stand_schema import StandCreateSchema, StandSchema

stand_service = StandService()
router = APIRouter(
    prefix="/stands",
    tags=["stands"],
    responses={404: {"description": "Not found"}},
)


@router.get('/', response_model=List[StandSchema])
def get_all_items():
    try:
        stands = stand_service.get()
        return stands.serialize()
    except Exception as ex:
        raise handle_exception(ex)


@router.get('/{stand_id}', response_model=StandSchema)
def get_stand(stand_id: int):
    try:
        stand = stand_service.get(stand_id)

        if stand:
            return stand.serialize()

        return JSONResponse(content={'message': 'Stand not found!'}, status_code=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        raise handle_exception(ex)


@router.post('/', response_model=StandSchema, status_code=status.HTTP_201_CREATED)
def add_stand(stand: StandCreateSchema):
    try:
        stand = stand_service.add(stand.dict())
        return stand.serialize()
    except Exception as ex:
        raise handle_exception(ex)


@router.put('/', response_model=StandSchema)
def update_stand(stand: StandSchema):
    try:
        stand = stand_service.update(stand.dict())
        return stand.serialize()
    except Exception as ex:
        raise handle_exception(ex)


@router.delete('/{stand_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_stand(stand_id):
    try:
        stand_service.delete(stand_id)
    except Exception as ex:
        raise handle_exception(ex)

def handle_exception(ex):
    message_error = str(ex)
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return HTTPException(status_code=status_code, detail=message_error)
