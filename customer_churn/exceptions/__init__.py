
class CustomException(Exception):
    """Custom exception for data ingestion errors."""
    def __init__(self, message, details=None):
        super().__init__(message)
        self.message=message
        self.details=details
