"""
General - not yet organized variables and functions.

### Usage:
```py
import xRedUtils.general as general
or
from xRedUtils import general
```
"""

import sys
sys.dont_write_bytecode = True
from xRedUtils.type_hints import SIMPLE_ANY

def palindrome(p: SIMPLE_ANY) -> bool:
    return str(p) == str(p)[::-1]