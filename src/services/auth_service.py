from utils.security import Security
from services.user_service import UserService
from exceptions.auth_exception import UnathorizedError
from models.user_group_enum import UserGroup


class AuthService:
    def __init__(self):
        self.user_service = UserService()
        self.security = Security()

    def login(self, user):
        user_database = self.user_service.get_by_email(
            user['email']
        ).serialize()

        if self.security.verify_password(user['password'], user_database['password']):
            data_token = {
                'id': user_database['id'],
                'user_group': user_database['user_group_id'],
            }
            return self.security.create_token(data_token)

        raise UnathorizedError('Invalid password')

    def register(self, user):
        user['user_group_id'] = UserGroup.CLIENT.value
        user = self.user_service.register(user)
        return user.serialize()
