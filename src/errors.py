"""
This module provides functions for generating error messages.

Functions:
- full_traceback: Generates a full traceback of the current exception as a string.
- simple_error: Formats a simple error message for an exception.

Usage:
import red_utils.errors as errors
or
from red_utils import errors
"""

import sys, traceback
sys.dont_write_bytecode = True

from .type_hints import SIMPLE_ANY


def full_traceback() -> str:
    """
    Generates a full traceback of the current `exception` as a string.

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