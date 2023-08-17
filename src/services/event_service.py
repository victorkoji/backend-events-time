from config.database_config import db
from models.event import EventModel
from exceptions.event_exception import NotFoundEventsError
from exceptions.general_exception import DatabaseError
from services.user_event_stand_service import UserEventStandService

class EventService:
    def __init__(self):
        self.user_event_stand_service = UserEventStandService()

    def get_all(self):
        query = db.table(EventModel.__table__).order_by('id', 'asc')
        events = query.get()
        return events.serialize()

    def get_event(self, event_id):
        event = EventModel.find(event_id)

        if event is None:
            raise NotFoundEventsError()

        return event.serialize()

    def get_all_events_by_user(self, user_id):
        events = self.user_event_stand_service.get_stand_by_user_event(user_id)
        return events

    def get_event_by_user(self, user_id, event_id):
        event = self.user_event_stand_service.get_stand_by_user_event(user_id, event_id)

        if len(event) == 0:
            raise NotFoundEventsError()

        return event[0]

    def add(self, data, user_id):
        event = EventModel()

        for key, value in data.items():
            setattr(event, key, value)

        event.user_created = user_id
        event.user_modified = user_id

        try:
            event.save()
        except:
            raise DatabaseError('Could not save!')

        return event

    def update(self, data):
        event = EventModel.find(data['id'])

        for key, value in data.items():
            setattr(event, key, value)

        try:
            event.save()
        except:
            raise DatabaseError('Could not update!')

        return event

    def delete(self, event_id):
        try:
            event = EventModel.find(event_id)
            event.delete()
        except:
            raise DatabaseError('Could not delete!')

        return event
