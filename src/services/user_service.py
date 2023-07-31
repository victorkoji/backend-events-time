from models.user import UserModel
from utils.security import Security
from exceptions.user_exception import DatabaseError


class UserService:
    def __init__(self):
        self.security = Security()

    def get(self, user_id=None):
        users = None

        if user_id:
            users = UserModel.find(user_id)
        else:
            users = UserModel.all()

        return users

    def get_by_email(self, email):
        return UserModel.find_by_column(email=email)

    def add(self, data):
        user = UserModel()
        data['password'] = self.security.create_password(data['password'])

        for key, value in data.items():
            setattr(user, key, value)

        try:
            user.save()
        except:
            raise DatabaseError('Could not save!')

        return user


    def update(self, data):
        user = UserModel.find(data['id'])

        for key, value in data.items():
            setattr(user, key, value)

        try:
            user.save()
        except:
            raise DatabaseError('Could not update!')

        return user


    def delete(self, product_id):
        try:
            user = UserModel.find(product_id)
            user.delete()
        except:
            raise DatabaseError('Could not delete!')

        return user
