from .custom_exception import CustomException

class DatabaseError(CustomException):
    def __init__(self, message="Error database"):
        super().__init__(message)


class NotFoundEventsError(CustomException):
    def __init__(self, message="Not Found Events"):
        super().__init__(message)
