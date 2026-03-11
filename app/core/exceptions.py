class AppException(Exception):
    """Base exception for the application."""
    pass

class InvalidAgeException(AppException):
    """Raised when an invalid age is provided."""
    def __init__(self, message: str = "Invalid age"):
        self.message = message
        super().__init__(self.message)
