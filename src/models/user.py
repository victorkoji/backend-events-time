from orator import SoftDeletes
from orator.orm import belongs_to
from models.user_group import UserGroupModel
from models.base_model import BaseModel


class UserModel(BaseModel, SoftDeletes):
    __schema__ = 'public'
    __table__ = 'users'
    __fillable__ = [
        'first_name', 'last_name', 'birth_date', 'email', 'cellphone', 'password', 'user_group_id', 'token_fcm'
    ]
    __guarded__ = ['id', 'password']
    __dates__ = ['deleted_at', 'birth_date']
    __timestamps__ = True

    @belongs_to
    def user_group(self):
        return UserGroupModel

    def get_dates(self):
        return ['created_at', 'updated_at', 'deleted_at']
