"""Typed errors raised by the API client."""


class APIError(Exception):
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code


class NotFoundError(APIError):
    pass


class AuthError(APIError):
    pass


class RateLimitError(APIError):
    pass


class ServerError(APIError):
    pass


class RequestTimeoutError(APIError):
    pass


class NetworkError(APIError):
    pass
