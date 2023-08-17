from .custom_exception import CustomException


class ProductFileNotFound(CustomException):
    def __init__(self, message="Product File Not Found"):
        super().__init__(message)

class UploadFailedError(CustomException):
    def __init__(self, message="Failed to upload"):
        super().__init__(message)
