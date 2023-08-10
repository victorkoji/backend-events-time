from models.user_event_stands import UserEventStandModel

class UserEventStandService:
    def __init__(self):
        pass

    def get_stand_by_user_event(self, user_id=None, event_id=None):

        events = UserEventStandModel.with_('event', 'stand') \
            .where('user_id', user_id)

        if event_id is not None:
            events.where('event_id', event_id)

        events = events.order_by('event_id').get()

        if events.is_empty():
            return []

        grouped_events = {}
        for event in events:
            if event.event_id not in grouped_events:
                grouped_events[event.event_id] = {
                    'id': event.event_id,
                    'name': event.event.name,
                    'programmed_date_initial': event.event.programmed_date_initial,
                    'programmed_date_final': event.event.programmed_date_final,
                    'is_public': event.event.is_public,
                    'stands': []
                }

            grouped_events[event.event_id]['stands'].append(event.stand.serialize())

        return list(grouped_events.values())
