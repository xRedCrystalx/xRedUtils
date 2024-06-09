"""
This module provides functions for generating error messages.

### Functions:
- `full_traceback` - Generates a full traceback of the current exception as a string.
- `simple_error` -  Formats a simple error message for an exception.

### Usage:
```py
import xRedUtils.errors as errors
or
from xRedUtils import errors
```
"""

import sys, traceback
sys.dont_write_bytecode = True

from .type_hints import SIMPLE_ANY

def full_traceback() -> str:
    """
    Generates a full traceback of the current `Exception` as a string.

    Returns:
    - A `string` containing the full traceback information.
    """
    return traceback.format_exc()

def simple_error(error: Exception) -> str:
    """
    Formats a simple error message for an exception.

    ### Parameters:
    - `error` - The `exception` for which to generate the error message.

    ### Returns:
    - A `string` containing a simple one line error.
    """
    return f"{type(error).__name__}: {error}"

class InvalidRootError(ArithmeticError):
    """Exception raised for mathematical roots"""
    pass

class NetworkError(ConnectionError):
    """Exception raised for network-related errors."""
    pass

class DatabaseConnectionError(ConnectionError):
    """Exception raised when a database connection fails."""
    pass

class AuthenticationError(PermissionError):
    """Exception raised for authentication failures."""
    pass

class AuthorizationError(PermissionError):
    """Exception raised for authorization failures."""
    pass

class ConfigurationError(BaseException):
    """Exception raised for configuration-related errors."""
    pass

class FileFormatError(TypeError):
    """Exception raised for errors related to file formats."""
    pass

class FileNotFoundError(FileExistsError):
    """Exception raised when a file is not found."""
    pass

class DataValidationError(ValueError):
    """Exception raised for data validation errors."""
    pass

class TimeoutError(RuntimeError):
    """Exception raised when an operation times out."""
    pass

class ResourceNotFoundError(MemoryError):
    """Exception raised when a requested resource is not found."""
    pass

class DependencyError(FileNotFoundError):
    """Exception raised when a dependency is missing or incorrect."""
    pass

class APIError(NetworkError):
    """Exception raised for errors related to API calls."""
    pass

class ServiceUnavailableError(NetworkError):
    """Exception raised when a service is unavailable."""
    pass

class InvalidInputError(ValueError):
    """Exception raised for invalid input errors."""
    pass

class RateLimitExceededError(NetworkError):
    """Exception raised when a rate limit is exceeded."""
    pass

class OperationNotPermittedError(RuntimeError):
    """Exception raised when an operation is not permitted."""
    pass

class IntegrityError(PermissionError):
    """Exception raised for data integrity issues."""
    pass

class VersionMismatchError(BaseException):
    """Exception raised when there is a version mismatch."""
    pass
