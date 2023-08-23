from typing import List
from fastapi import APIRouter, Response, status, HTTPException, Depends

from services.event_service import EventService
from schemas.event_schema import EventCreateSchema, EventSchema
from controllers.dependencies.user_dependency import get_user_token
from exceptions.event_exception import NotFoundEventsError


event_service = EventService()
router = APIRouter(
    prefix="/events",
    tags=["events"],
    responses={404: {"description": "Not found"}},
)


@router.get('/', response_model=List[EventSchema])
def get_all_items():
    try:
        return event_service.get_all()
    except Exception as ex:
        raise handle_exception(ex)


@router.get('/{event_id}', response_model=EventSchema)
def get_event(event_id: int):
    try:
        return event_service.get_event(event_id)
    except Exception as ex:
        raise handle_exception(ex)


@router.post('/', response_model=EventSchema, status_code=status.HTTP_201_CREATED)
def add_event(event: EventCreateSchema, user: dict = Depends(get_user_token)):
    try:
        event = event_service.add(event.dict(), user['sub'])

        return event.serialize()
    except Exception as ex:
        raise handle_exception(ex)


@router.put('/', response_model=EventSchema)
def update_event(event: EventSchema):
    try:
        event = event_service.update(event.dict())
        return event.serialize()
    except Exception as ex:
        raise handle_exception(ex)


@router.delete('/{event_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_event(event_id):
    try:
        event_service.delete(event_id)
    except Exception as ex:
        raise handle_exception(ex)

def handle_exception(ex):
    message_error = str(ex)

    if isinstance(ex, NotFoundEventsError):
        status_code = status.HTTP_404_NOT_FOUND
    else:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return HTTPException(status_code=status_code, detail=message_error)
