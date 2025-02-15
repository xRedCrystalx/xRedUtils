"""
This module provides async functions for working with objects (classes).

### Functions:
- `get_full_object_path` - Finds full python path of the object, object method or type.
- `get_object_module_path` - Finds object's module python path.
- `get_object_name` - Finds object's name.
- `extract_attributes` - Extract all attributes from an object and return as a dictionary.
- `get_inheritance_layers` - Get the inheritance layers (method resolution order) for a given `object` or `type`.
- `get_all_running_objects` - Returns all objects that are being tracked by the garabge collector (`gc`)

### Usage:
```py

import xRedUtilsAsync.objects as objects
or
from xRedUtilsAsync import objects
```
"""

import sys, gc
sys.dont_write_bytecode = True
from .annotations import Any, MethodType

__all__: tuple[str, ...] = (
    "get_full_object_path", "get_object_module_path", "get_object_name", "extract_attributes", "get_inheritance_layers", "get_all_running_objects"
)

async def get_full_object_path(obj: object | MethodType | type) -> str:
    """
    Finds full python path of the object, object method or type.

    ### Parameters:
    - `obj` - Object, object method or type to check. 

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
    - `obj` - Object, object method or type to check.

    ### Returns:
    - Module python path.
    """
    return obj.__module__

async def get_object_name(obj: type | object) -> str:
    """
    Finds object's name.

    ### Parameters:
    - `obj` - Object or type to check. 

    ### Returns:
    - Name of object.
    """
    return obj.__name__

async def extract_attributes(obj: object) -> dict[str, Any]:
    """
    Extract all attributes from an object and return as a dictionary.

    ### Parameters:
    - `obj` - Object to extract attributes from. 

    ### Returns:
    - Dictionary with `attr: value`.
    """
    return {attr: getattr(obj, attr) for attr in dir(obj) if not attr.startswith("__")}

async def get_inheritance_layers(obj: object | type) -> list[type]:
    """
    Get the inheritance layers (method resolution order) for a given `object` or `type`.
    
    ### Parameters:
    - `obj` - The `object` or `type` to inspect.

    ### Returns:
    - A `list` of `types` starting from the given `object's type` descending through chain.
    """
    
    if isinstance(obj, type):
        return obj.mro()

    return obj.__class__.mro()

async def get_all_running_objects(_type: type = None) -> list[object]:
    """
    Returns all objects that are being tracked by the garabge collector (`gc`)

    ### Parameters:
    - `_type` - If provided, only objects that are instances of this `type` are returned.

    ### Returns:
    - A `list` of tracked objects, excluding the returned list itself.
    """
    if _type:
        return [o for o in gc.get_objects() if isinstance(o, _type)]

    return gc.get_objects()
