"""
This module provides async functions to deal with functions. Yeah makes no sense.

### Functions:
- `safe_call` - Safely calls a function with given arguments and keyword arguments.

### Usage:
```py

import xRedUtilsAsync.funcs as funcs
or
from xRedUtilsAsync import funcs
```
"""

import sys, asyncio
sys.dont_write_bytecode = True
from typing import Callable, Literal, overload

from .type_hints import SIMPLE_ANY
from .errors import full_traceback, simple_error

__all__: tuple[str, ...] = (
    "safe_call",
)

@overload
async def safe_call(func: Callable, args: tuple | list = None, kwargs: dict[str, SIMPLE_ANY] = None) -> SIMPLE_ANY: ...
@overload
async def safe_call(func: Callable, args: tuple | list = None, kwargs: dict[str, SIMPLE_ANY] = None, _default: SIMPLE_ANY = None, _error: Literal["simple", "full", "none"] = "simple") -> SIMPLE_ANY: ...

async def safe_call(func: Callable, args: tuple | list = None, kwargs: dict[str, SIMPLE_ANY] = None, _default: SIMPLE_ANY = None, _error: Literal["simple", "full", "none"] = "simple") -> SIMPLE_ANY:
    """
    Safely calls a function with given arguments and keyword arguments. If an exception occurs,
    it handles the exception based on the specified error handling mode and returns a default value.

    ### Parameters:
    - `func` - The function to be called.
    - `args` - The positional arguments to be passed to the function.
    - `kwargs` - The keyword arguments to be passed to the function.
    
    - `_default` - The default value to return in case of an exception. Defaults to `None`.
    - `_error` - The error handling mode. "simple" prints a simple error message,
      while "full" returns the full traceback. Defaults to `"simple"`.

    ### Returns:
    - The return value of the function if successful, otherwise the `_default` value.
    """
    args = args if args and isinstance(args, tuple | list) else []
    kwargs = kwargs if kwargs and isinstance(kwargs, dict) else {}

    try:
        return await func(*args, **kwargs) if asyncio.iscoroutine(func) else func(*args, **kwargs)
    except Exception:
        if _error != "none":
            print(await simple_error() if _error == "simple" else await full_traceback())

    return _default
