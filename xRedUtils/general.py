"""
General - not yet organized variables and functions.

### Usage:
```py
import xRedUtils.general as general
or
from xRedUtils import general
```
"""

import sys, uuid
sys.dont_write_bytecode = True
from xRedUtils.type_hints import SIMPLE_ANY

def isPalindrome(p: SIMPLE_ANY) -> bool:
    """
    Checks if the `string` representation of any datatype is palindrome.

    ### Parameters:
    - `p` - Argument that gets checked.

    ### Returns:
    - `True` if its palindrome, otherwise `False`
    """
    return str(p) == str(p)[::-1]

def generate_uuid() -> str:
    """
    Generates a random UUID
    """
    return str(uuid.uuid4())