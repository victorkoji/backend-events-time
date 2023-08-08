from .custom_exception import CustomException

class DatabaseError(CustomException):
    def __init__(self, message="Error database"):
        super().__init__(message)


class EmailAlreadyExistError(CustomException):
    def __init__(self, message="Email already exist"):
        super().__init__(message)
