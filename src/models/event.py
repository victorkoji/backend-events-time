from orator import SoftDeletes
from models.base_model import BaseModel


class EventModel(BaseModel, SoftDeletes):
    __schema__ = 'public'
    __table__ = 'events'
    __fillable__ = ['name', 'address', 'is_public']
    __dates__ = ['deleted_at', 'programmed_date_initial',
                 'programmed_date_final']
    __timestamps__ = True

    def get_dates(self):
        return ['created_at', 'updated_at', 'deleted_at']
