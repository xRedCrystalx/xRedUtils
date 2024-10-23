"""
This module provides async functions for working with objects (classes).

### Functions:
- `get_full_object_path` - Finds full python path of the object, object method or type.
- `get_object_module_path` - Finds object's module python path.
- `get_object_name` - Finds object's name.
- `extract_attributes` - Extract all attributes from an object and return as a dictionary.

### Usage:
```py

import xRedUtilsAsync.objects as objects
or
from xRedUtilsAsync import objects
```
"""

import sys
sys.dont_write_bytecode = True
from types import MethodType

from .type_hints import SIMPLE_ANY

__all__: tuple[str, ...] = (
    "get_full_object_path", "get_object_module_path", "get_object_name"
)

async def get_full_object_path(obj: object | MethodType | type) -> str:
    """
    Finds full python path of the object, object method or type.

    ### Parameters:
    - `obj` - (Called) object, object method or type to check. 

    ### Returns:
    - Full python path of the object.
    """
    if isinstance(obj, type | MethodType):
        return f"{obj.__module__}.{obj.__qualname__}"
        
    return f"{obj.__class__.__module__}.{obj.__class__.__qualname__}"

async def get_object_module_path(obj: object | MethodType | type) -> str:
    """
    Finds object's module python path.

    ### Parameters:
    - `obj` - (Called) object, object method or type to check. 

    ### Returns:
    - Module python path.
    """
    return obj.__module__

async def get_object_name(obj: type | object) -> str:
    """
    Finds object's name.

    ### Parameters:
    - `obj` - (Called) object or type to check. 

    ### Returns:
    - Name of object.
    """
    return obj.__name__

async def extract_attributes(obj: object) -> dict[str, SIMPLE_ANY]:
    """
    Extract all attributes from an object and return as a dictionary.

    ### Parameters:
    - `obj` - (Called) object.

    ### Returns:
    - Dictionary with attr: value.
    """
    return {attr: getattr(obj, attr) for attr in dir(obj) if not attr.startswith("__")}
