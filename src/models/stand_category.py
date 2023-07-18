from orator import SoftDeletes
from models.base_model import BaseModel


class StandCategoryModel(BaseModel, SoftDeletes):
    __schema__ = 'public'
    __table__ = 'stand_categories'
    __fillable__ = ['name', 'event_id']
    __dates__ = ['deleted_at']
    __timestamps__ = True
