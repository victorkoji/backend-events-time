from orator import SoftDeletes
from models.base_model import BaseModel


class UserGroupModel(BaseModel, SoftDeletes):
    __schema__ = 'public'
    __table__ = 'user_groups'
    __fillable__ = ['name']
    __dates__ = ['deleted_at']
    __timestamps__ = True
