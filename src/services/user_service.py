from models.user import UserModel
from utils.security import Security


class UserService:
    def __init__(self):
        self.security = Security()

    def get(self, id=None):
        users = None

        if id:
            users = UserModel.find(id)
        else:
            users = UserModel.all()

        return users

    def get_by_email(self, email):
        return UserModel.find_by_column(email=email)

    def add(self, data):
        try:
            user = UserModel()
            data['password'] = self.security.create_password(data['password'])

            for key, value in data.items():
                setattr(user, key, value)

            user.save()

            return user
        except:
            raise Exception('Could not save!')

    def update(self, data):
        try:
            user = UserModel.find(data['id'])

            for key, value in data.items():
                setattr(user, key, value)

            user.save()

            return user
        except:
            raise Exception('Could not update!')

    def delete(self, product_id):
        try:
            user = UserModel.find(product_id)
            user.delete()
        except:
            raise Exception('Could not delete!')

        return user
