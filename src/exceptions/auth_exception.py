from .custom_exception import CustomException

class UnathorizedError(CustomException):
    def __init__(self, message="Unathorized"):
        super().__init__(message)
