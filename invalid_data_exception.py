class InvalidDataException(Exception):
    """Custom exception for invalid business data validation."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
