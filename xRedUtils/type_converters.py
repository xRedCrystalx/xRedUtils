"""
Basic python type converters with error handlers.

### Functions:
- `to_str` - Tries to convert given object to string.
- `to_int` - Tries to convert given object to integer.
- `to_float` - Tries to convert given object to float.
- `to_bool` - Tries to convert given object to boolean.
- `to_tuple` - Tries to convert given object to tuple.
- `to_list` - Tries to convert given object to list.
- `to_dict` - Tries to convert given object to dictionary.
- `to_set` - Tries to convert given object to set.
- `to_frozen_set` - Tries to convert given object to frozen set.
- `to_bytes` - Tries to convert given object to bytes.
- `to_byte_array` - Tries to convert given object to byte array.
- `to_none` - Always returns `None`.

### Usage:
```py

import xRedUtils.type_converters as type_converters
or
from xRedUtils import type_converters
```
"""

import sys
sys.dont_write_bytecode = True
from .type_hints import SIMPLE_ANY


def to_str(obj: SIMPLE_ANY) -> str | SIMPLE_ANY:
    """
    Tries to convert given object to string.
    
    ### Parameters:
    - `obj` - Object that needs to be converted.

    ### Returns:
    - `String` representation of the object OR itself if conversion failed.
    """
    try: return str(obj)
    except: return obj

def to_int(obj: SIMPLE_ANY) -> int | SIMPLE_ANY:
    """
    Tries to convert given object to integer.
    
    ### Parameters:
    - `obj` - Object that needs to be converted.

    ### Returns:
    - `Integer` representation of the object OR itself if conversion failed.
    """
    try: return int(obj)
    except: return obj

def to_float(obj: SIMPLE_ANY) -> float | SIMPLE_ANY:
    """
    Tries to convert given object to float.
    
    ### Parameters:
    - `obj` - Object that needs to be converted.

    ### Returns:
    - `Float` representation of the object OR itself if conversion failed.
    """
    try: return float(obj)
    except: return obj

def to_bool(obj: SIMPLE_ANY) -> bool | SIMPLE_ANY:
    """
    Tries to convert given object to boolean.
    
    ### Parameters:
    - `obj` - Object that needs to be converted.

    ### Returns:
    - `Boolean` representation of the object OR itself if conversion failed.
    """
    try: return bool(obj)
    except: return obj

def to_tuple(obj: SIMPLE_ANY) -> tuple | SIMPLE_ANY:
    """
    Tries to convert given object to tuple.
    
    ### Parameters:
    - `obj` - Object that needs to be converted.

    ### Returns:
    - `Tuple` representation of the object OR itself if conversion failed.
    """
    try: return tuple(obj)
    except: return obj

def to_list(obj: SIMPLE_ANY) -> list | SIMPLE_ANY:
    """
    Tries to convert given object to list.
    
    ### Parameters:
    - `obj` - Object that needs to be converted.

    ### Returns:
    - `List` representation of the object OR itself if conversion failed.
    """
    try: return list(obj)
    except: return obj

def to_dict(obj: SIMPLE_ANY) -> dict | SIMPLE_ANY:
    """
    Tries to convert given object to dictionary.
    
    ### Parameters:
    - `obj` - Object that needs to be converted.

    ### Returns:
    - `Dictionary` representation of the object OR itself if conversion failed.
    """
    try: return dict(obj)
    except: return obj

def to_set(obj: SIMPLE_ANY) -> set | SIMPLE_ANY:
    """
    Tries to convert given object to set.
    
    ### Parameters:
    - `obj` - Object that needs to be converted.

    ### Returns:
    - `Set` representation of the object OR itself if conversion failed.
    """
    try: return set(obj)
    except: return obj

def to_frozen_set(obj: SIMPLE_ANY) -> frozenset | SIMPLE_ANY:
    """
    Tries to convert given object to frozen set.
    
    ### Parameters:
    - `obj` - Object that needs to be converted.

    ### Returns:
    - `Frozen set` representation of the object OR itself if conversion failed.
    """
    try: return frozenset(obj)
    except: return obj

def to_bytes(obj: SIMPLE_ANY, *args, **kwargs) -> bytes | SIMPLE_ANY:
    """
    Tries to convert given object to bytes.
    
    ### Parameters:
    - `obj` - Object that needs to be converted.
    
    *args, **kwargs -> params for `bytes` object

    ### Returns:
    - `Bytes` representation of the object OR itself if conversion failed.
    """
    try: return bytes(obj, *args, **kwargs)
    except: return obj

def to_byte_array(obj: SIMPLE_ANY, *args, **kwargs) -> bytearray | SIMPLE_ANY:
    """
    Tries to convert given object to bytearray.
    
    ### Parameters:
    - `obj` - Object that needs to be converted.
    
    *args, **kwargs -> params for `bytes` object

    ### Returns:
    - `Bytearray` representation of the object OR itself if conversion failed.
    """
    try: return bytearray(obj, *args, **kwargs)
    except: return obj


def to_none(obj: SIMPLE_ANY) -> None:
    """
    Always returns `None`.
    """
    return None
