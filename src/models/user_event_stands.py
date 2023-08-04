from orator import SoftDeletes
from orator.orm import belongs_to
from models.base_model import BaseModel
from models.stand import StandModel
from models.event import EventModel
from models.user import UserModel


class UserEventStandModel(BaseModel, SoftDeletes):
    __schema__ = 'public'
    __table__ = 'user_event_stands'
    __fillable__ = ['user_id', 'stand_id', 'event_id', 'is_responsible']
    __dates__ = ['deleted_at']
    __timestamps__ = True

    @belongs_to
    def user(self):
        return UserModel

    @belongs_to
    def stand(self):
        return StandModel

    @belongs_to
    def event(self):
        return EventModel
