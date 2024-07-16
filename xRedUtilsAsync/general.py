"""
General - not yet organized variables and async functions.

### Functions:
- `isPalindrome` - Checks if the `string` representation of any datatype is palindrome.
- `generate_uuid` - Generates a random UUID.

### Usage:
```py

import xRedUtilsAsync.general as general
or
from xRedUtilsAsync import general
```
"""

import sys, uuid
sys.dont_write_bytecode = True
from .type_hints import SIMPLE_ANY

__all__: tuple[str, ...] = (
    "isPalindrome", "generate_uuid"
)

async def isPalindrome(p: SIMPLE_ANY) -> bool:
    """
    Checks if the `string` representation of any datatype is palindrome.

    ### Parameters:
    - `p` - Argument that gets checked.

    ### Returns:
    - `True` if its palindrome, otherwise `False`
    """
    return str(p) == str(p)[::-1]

async def generate_uuid() -> str:
    """
    Generates a random UUID.
    """
    return str(uuid.uuid4())