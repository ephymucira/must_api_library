class MustAPIError(Exception):
    """Base exception for MustAPI errors."""
    def __init__(self, message: str, status_code: int = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class AuthenticationError(MustAPIError):
    """Raised when authentication fails."""
    pass

class ResourceNotFoundError(MustAPIError):
    """Raised when a requested resource is not found."""
    pass

class ValidationError(MustAPIError):
    """Raised when data validation fails."""
    pass

class RateLimitError(MustAPIError):
    """Raised when API rate limit is exceeded."""
    pass