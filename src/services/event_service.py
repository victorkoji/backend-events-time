from models.event import EventModel


class EventService:
    def __init__(self):
        pass

    def get(self, id=None):
        events = None

        if id:
            events = EventModel.find(id)
        else:
            events = EventModel.all()

        return events

    def add(self, data):
        try:
            event = EventModel()

            for key, value in data.items():
                setattr(event, key, value)

            event.user_created = 1
            event.user_modified = 1

            event.save()

            return event
        except:
            raise Exception('Could not save!')

    def update(self, data):
        try:
            event = EventModel.find(data['id'])

            for key, value in data.items():
                setattr(event, key, value)

            event.save()

            return event
        except:
            raise Exception('Could not update!')

    def delete(self, event_id):
        try:
            event = EventModel.find(event_id)
            event.delete()
        except:
            raise Exception('Could not delete!')

        return event
