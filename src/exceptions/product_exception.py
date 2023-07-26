class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class DatabaseError(CustomException):
    def __init__(self, message="Error database"):
        super().__init__(message)


class ProductNotFound(CustomException):
    def __init__(self, message="Product Not Found"):
        super().__init__(message)
