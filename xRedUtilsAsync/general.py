"""
General - not yet organized variables and async functions.

### CONSTANTS:
- `TIME_UNITS` - Conversion from `str` to `int` eg. `"minute": 60`

### Functions:
- `isPalindrome` - Checks if the `string` representation of any datatype is palindrome.

### Usage:
```py

import xRedUtilsAsync.general as general
or
from xRedUtilsAsync import general
```
"""

import sys
sys.dont_write_bytecode = True
from .annotations import Any

__all__: tuple[str, ...] = (
    "TIME_UNITS",
    "isPalindrome"
)

TIME_UNITS: dict[str, int] = {
    "second": 1,
    "minute": 60,
    "hour": 3_600,
    "day": 86_400,
    "week": 604_800,
    "month": 2_592_000,          # 30 days
    "year": 31_536_000,          # actual 365 days
    "decade": 315_532_800,
    "century": 3_155_673_600,
    "millenium": 31_556_908_800
}

async def isPalindrome(p: Any) -> bool:
    """
    Checks if the `string` representation of any datatype is palindrome.

    ### Parameters:
    - `p` - Argument that gets checked.

    ### Returns:
    - `True` if its palindrome, otherwise `False`
    """
    return str(p) == str(p)[::-1]
