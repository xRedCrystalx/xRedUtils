"""
All important type annotations.

- Merges together everything from typing and types.
- Implements Generic types-
- Optional typing imports from `numpy` and `pandas`, if present. 

### Usage:
```py

import xRedUtils.annotations as annotations
or
from xRedUtils import annotations
```
"""

import sys
sys.dont_write_bytecode = True
from typing import *
from types import *

# i guess useful?
try:
    from numpy.typing import *
except: pass

try:
    from pandas._typing import *
except: pass

# Generics
T = TypeVar("T")    # TYPE
K = TypeVar("K")    # KEY
V = TypeVar("V")    # VALUE
F = TypeVar("F")    # FUNCTION
M = TypeVar("M")    # METHOD/MODULE
O = TypeVar("O")    # OBJECT

NUMBER = int | float | complex
BINARY = bytes | bytearray | memoryview
ITERABLE = list | tuple | set | frozenset | range | map | filter | zip

BUILTINS = NUMBER | BINARY | ITERABLE | str | bool | Exception | slice | object | type | dict | None
