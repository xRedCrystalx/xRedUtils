"""
General - not yet organized variables and functions.

### Functions:
- `isPalindrome` - Checks if the `string` representation of any datatype is palindrome.

### Usage:
```py

import xRedUtils.general as general
or
from xRedUtils import general
```
"""

import sys
sys.dont_write_bytecode = True
from .type_hints import SIMPLE_ANY

__all__: tuple[str, ...] = (
    "isPalindrome"
)

def isPalindrome(p: SIMPLE_ANY) -> bool:
    """
    Checks if the `string` representation of any datatype is palindrome.

    ### Parameters:
    - `p` - Argument that gets checked.

    ### Returns:
    - `True` if its palindrome, otherwise `False`
    """
    return str(p) == str(p)[::-1]
