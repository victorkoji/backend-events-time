from orator import SoftDeletes
from models.base_model import BaseModel
from models.stand_category import StandCategoryModel
from models.event import EventModel
from orator.orm import belongs_to


class StandModel(BaseModel, SoftDeletes):
    __schema__ = 'public'
    __table__ = 'stands'
    __fillable__ = ['name', 'is_cashier', 'stand_category_id', 'event_id']
    __dates__ = ['deleted_at']
    __timestamps__ = True

    @belongs_to
    def stand_category(self):
        return StandCategoryModel

    @belongs_to
    def event(self):
        return EventModel
