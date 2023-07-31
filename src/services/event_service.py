from models.event import EventModel
from exceptions.event_exception import DatabaseError


class EventService:
    def __init__(self):
        pass

    def get(self, event_id=None):
        events = None

        if event_id:
            events = EventModel.find(event_id)
        else:
            events = EventModel.all()

        return events

    def add(self, data):
        event = EventModel()

        for key, value in data.items():
            setattr(event, key, value)

        event.user_created = 1
        event.user_modified = 1

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
