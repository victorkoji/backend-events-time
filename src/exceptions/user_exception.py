from .custom_exception import CustomException


class EmailAlreadyExistError(CustomException):
    def __init__(self, message="Email already exist"):
        super().__init__(message)
