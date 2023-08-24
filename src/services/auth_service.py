import os

from datetime import timedelta
from utils.security import Security
from services.user_service import UserService
from exceptions.auth_exception import UnathorizedError
from models.enums.user_group_enum import UserGroup

class AuthService:
    def __init__(self):
        self.user_service = UserService()
        self.security = Security()

        self.access_token_secret_key = os.getenv("AUTH_ACCESS_TOKEN_SECRET_KEY")
        self.access_token_algorithm = os.getenv("AUTH_ACCESS_TOKEN_SECRET_ALGORITHM")
        self.access_token_expires_minutes = int(os.getenv("AUTH_ACCESS_TOKEN_EXPIRE_MINUTES"))

        self.refresh_token_secret_key = os.getenv("AUTH_REFRESH_TOKEN_SECRET_KEY")
        self.refresh_token_algorithm = os.getenv("AUTH_REFRESH_TOKEN_SECRET_ALGORITHM")
        self.refresh_token_expires_days = int(os.getenv("AUTH_REFRESH_TOKEN_EXPIRE_DAYS"))

    def login(self, user: dict) -> dict:
        user_database = self.user_service.get_by_email(
            user['email']
        ).serialize()

        if self.security.verify_password(user['password'], user_database['password']):
            data_token = {
                'sub': str(user_database['id']),
                'user_group': user_database['user_group_id'],
            }

            return self._generate_token(data_token)

        raise UnathorizedError('Invalid password')

    def register(self, user: dict):
        user['user_group_id'] = UserGroup.CLIENT.value
        user = self.user_service.register(user)
        return user.serialize()

    def refresh_token(self, refresh_token: str) -> dict:
        token = self.get_refresh_token(refresh_token)

        if not token:
            raise UnathorizedError("Invalid token or expired token.")

        user_id = token.get("sub")
        user_database = self.user_service.get(user_id).serialize()

        data_token = {
            'sub': user_database['id'],
            'user_group': user_database['user_group_id'],
        }

        return self._generate_token(data_token)

    def get_access_token(self, token: str) -> str:
        return self.security.get_decode_token(token, self.access_token_secret_key, self.access_token_algorithm)

    def get_refresh_token(self, token: str) -> str:
        return self.security.get_decode_token(token, self.refresh_token_secret_key, self.refresh_token_algorithm)

    def _generate_token(self, data_token: dict) -> dict:
        access_token_expires = timedelta(minutes=self.access_token_expires_minutes)
        access_token = self.security.create_token(
            data_token, self.access_token_secret_key, self.access_token_algorithm, access_token_expires
        )

        refresh_token_expires = timedelta(days=self.refresh_token_expires_days)
        refresh_token = self.security.create_token(
            data_token, self.refresh_token_secret_key, self.refresh_token_algorithm, refresh_token_expires
        )

        return {
            "access_token": access_token, 
            "refresh_token": refresh_token
        }
