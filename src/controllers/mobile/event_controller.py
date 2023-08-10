from typing import List
from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse

from services.event_service import EventService
from schemas.event_schema import EventByUserSchema
from controllers.dependencies.user_dependency import get_user_token
from exceptions.event_exception import NotFoundEventsError


event_service = EventService()
router = APIRouter(
    prefix="/mobile/events",
    tags=["events"],
    responses={404: {"description": "Not found"}},
)


@router.get('/', response_model=List[EventByUserSchema])
def get_all_events_by_user(user: dict = Depends(get_user_token)):
    try:
        events = event_service.get_all_events_by_user(user['id'])
        return events
    except Exception as ex:
        raise handle_exception(ex)


@router.get('/{event_id}', response_model=EventByUserSchema)
def get_event_by_user(event_id: int, user: dict = Depends(get_user_token)):
    try:
        event = event_service.get_event_by_user(user['id'], event_id)

        if event:
            return event

        return JSONResponse(content={'message': 'Event not found!'}, status_code=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        raise handle_exception(ex)

def handle_exception(ex):
    message_error = str(ex)

    if isinstance(ex, NotFoundEventsError):
        status_code = status.HTTP_404_NOT_FOUND
    else:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return HTTPException(status_code=status_code, detail=message_error)
