from models.user import UserModel
from utils.security import Security
from exceptions.user_exception import EmailAlreadyExistError, NotFoundUserError
from exceptions.general_exception import DatabaseError


class UserService:
    def __init__(self):
        self.security = Security()

    def get(self, user_id: int = None):
        users = None

        if user_id:
            users = UserModel.find(user_id)
        else:
            users = UserModel.all()

        return users

    def get_by_email(self, email: str):
        return UserModel.find_by_column(email=email)

    def add(self, data: dict):
        user = UserModel()
        data['password'] = self.security.create_password(data['password'])

        for key, value in data.items():
            setattr(user, key, value)

        try:
            user.save()
        except:
            raise DatabaseError('Could not save!')

        return user

    def register(self, data: dict):
        user_exists = self.get_by_email(data['email'])

        if user_exists is not None:
            raise EmailAlreadyExistError()

        user = UserModel()
        data['password'] = self.security.create_password(data['password'])

        for key, value in data.items():
            setattr(user, key, value)

        try:
            user.save()
        except:
            raise DatabaseError('Could not save!')

        return user

    def update(self, data: dict):
        user = UserModel.find(data['id'])

        for key, value in data.items():
            setattr(user, key, value)

        try:
            user.save()
        except:
            raise DatabaseError('Could not update!')

        return user


    def delete(self, user_id: int):
        try:
            user = UserModel.find(user_id)
            user.delete()
        except:
            raise DatabaseError('Could not delete!')

        return user


    def add_token_fcm(self, user_id: int, data: dict):
        user = UserModel.find(user_id)

        if user is None:
            raise NotFoundUserError()

        user.token_fcm = data.get('token_fcm')

        try:
            user.save()
        except:
            raise DatabaseError('Could not added!')

        return user


    def delete_token_fcm(self, user_id: int):
        user = UserModel.find(user_id)

        if user is None:
            raise NotFoundUserError()

        user.token_fcm = None

        try:
            user.save()
        except:
            raise DatabaseError('Could not delete!')

        return user
