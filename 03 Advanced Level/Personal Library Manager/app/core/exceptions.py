# app/core/exceptions.py

class AppException(Exception):
    pass

class ResourceNotFoundError(AppException):
    def __init__(self, resource: str, identifier: str):
        self.message = f"{resource} with identifier '{identifier}' not found"
        super().__init__(self.message)

class AlreadyExistsError(AppException):
    def __init__(self, resource: str, identifier: str):
        self.message = f"{resource} with identifier '{identifier}' already exists"
        super().__init__(self.message)

class InvalidCredentialsError(AppException):
    """ Used for wrong passwords or login failures """
    def __init__(self, message: str = "Invalid credentials"):
        self.message = message
        super().__init__(self.message)