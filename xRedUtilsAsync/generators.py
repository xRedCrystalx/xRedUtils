"""
This module provides async functions for working with hashes and hashing.

### Functions:
- `generate_uuid` - Generates a random UUID.
- `generate_string` - Generates a random string.

### Usage:
```py

import xRedUtils.generators as generators
or
from xRedUtils import generators
```
"""

import sys, random, uuid
sys.dont_write_bytecode = True
from typing import Literal, overload

from .strings import ASCII_LOWERCASE, ASCII_UPPERCASE, PUNCTUATION, DIGITS

__all__: tuple[str, ...] = (
    "generate_uuid", "generate_string"
)

async def generate_uuid() -> uuid.UUID:
    """
    Generates a random UUID.

    ### Returns:
    - An `UUID` object - use `str()` to convert it to `string`. 
    """
    return uuid.uuid4()

@overload
async def generate_string(length: int, upper: bool = True, lower: bool = True) -> str: ...
@overload
async def generate_string(length: int, upper: bool = True, lower: bool = True, puncs: bool = False) -> str: ...
@overload
async def generate_string(length: int, upper: bool = True, lower: bool = True, digits: bool = False) -> str: ...
@overload
async def generate_string(length: int, upper: bool = True, lower: bool = True, digits: bool = False, puncs: bool = False) -> str: ...

async def generate_string(length: int, upper: bool = True, lower: bool = True, digits: bool = False, puncs: bool = False) -> str:
    """
    Generates a random string.
    
    ### Parameters:
    - `length` - `Integer` specifiying the size of returned string.
    - `upper` - Use uppercased letters?
    - `lower` - Use lowercased letters?
    - `digits` - Use digits/numbers?
    - `puncs` - Use punctuations?

    ### Returns:
    - A `string` made of chars of specified length.
    """

    char_types: dict[bool, str] = {
        lower: ASCII_LOWERCASE,
        upper: ASCII_UPPERCASE,
        digits: DIGITS,
        puncs: PUNCTUATION,
    }
    
    chars: str = "".join(value for key, value in char_types.items() if key)
    
    if not chars:
        raise ValueError("At least one character type must be enabled.")
    
    return "".join(random.choices(chars, k=length))

