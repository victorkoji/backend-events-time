from .custom_exception import CustomException

class DatabaseError(CustomException):
    def __init__(self, message="Error database"):
        super().__init__(message)


class ProductNotFound(CustomException):
    def __init__(self, message="Product Not Found"):
        super().__init__(message)
