class DatabaseError(BaseException):
    def __init__(self, message, details=None):
        self.message = message
        self.details = details

        super().__init__(message, details)

    def __str__(self):
        return self.message
