from .custom_exception import CustomException

class NotFoundEventsError(CustomException):
    def __init__(self, message="Not Found Events"):
        super().__init__(message)
