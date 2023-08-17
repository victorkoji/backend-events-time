from .custom_exception import CustomException


class ProductNotFound(CustomException):
    def __init__(self, message="Product Not Found"):
        super().__init__(message)
