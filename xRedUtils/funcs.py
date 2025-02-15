"""
This module provides functions to deal with functions. Yeah makes no sense.

### Functions:
- `safe_call` - Safely calls a function with given arguments and keyword arguments.

### Usage:
```py

import xRedUtils.funcs as funcs
or
from xRedUtils import funcs
```
"""

import sys
sys.dont_write_bytecode = True
from .annotations import Any, ITERABLE, Callable, Literal, overload
from .errors import full_traceback, simple_error

__all__: tuple[str, ...] = (
    "safe_call",
)

@overload
def safe_call(func: Callable, args: tuple | list = None, kwargs: dict[str, Any] = None) -> Any: ...
@overload
def safe_call(func: Callable, args: tuple | list = None, kwargs: dict[str, Any] = None, _default: Any = None, _error: Literal["simple", "full", "none"] = "simple") -> Any: ...

def safe_call(func: Callable, args: tuple | list = None, kwargs: dict[str, Any] = None, _default: Any = None, _error: Literal["simple", "full", "none"] = "simple") -> Any:
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
    args = args if args and isinstance(args, ITERABLE) else []
    kwargs = kwargs if kwargs and isinstance(kwargs, dict) else {}

    try:
        return func(*args, **kwargs)
    except Exception as error:
        if _error != "none":
            print(simple_error(error) if _error == "simple" else full_traceback(error))

    return _default
