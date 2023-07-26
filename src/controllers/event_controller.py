from fastapi import APIRouter, Response, status
from services.event_service import EventService
from schemas.event_schema import EventCreateSchema, EventSchema
from fastapi.responses import JSONResponse
from typing import List

event_service = EventService()
router = APIRouter(
    prefix="/events",
    tags=["events"],
    responses={404: {"description": "Not found"}},
)


@router.get('/', response_model=List[EventSchema])
def get_all_items():
    try:
        events = event_service.get()
        return events.serialize()
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.get('/{event_id}', response_model=EventSchema)
def get_event(event_id: int):
    try:
        event = event_service.get(event_id)
        if (event):
            return event.serialize()
        else:
            return JSONResponse(content={'message': 'Event not found!'}, status_code=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.post('/', response_model=EventSchema, status_code=status.HTTP_201_CREATED)
def add_event(event: EventCreateSchema):
    try:
        print(event.dict())

        event = event_service.add(event.dict())
        print(event.serialize())
        return event.serialize()
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.put('/', response_model=EventSchema)
def update_event(event: EventSchema):
    try:
        event = event_service.update(event.dict())
        return event.serialize()
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.delete('/{event_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_event(event_id):
    try:
        event_service.delete(event_id)
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)
