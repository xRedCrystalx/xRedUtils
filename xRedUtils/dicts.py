"""
This module provides functions for working with dictionaries and JSON data.

### Functions:
- `dict_walk` - Recursively walks through a dictionary to retrieve a value specified by a given path.
- `value_exist` - Checks whether a value exists within a dictionary at the specified path.
- `dict_merge` - Merges two dictionaries.
- `flatten_dict` - Flattens a nested dictionary into a single-level dictionary.
- `json_to_dict` - Converts JSON data to a Python dictionary.
- `dict_to_json` - Converts a dictionary to a JSON string with optional indentation and additional keyword arguments.

### Usage:
```py

import xRedUtils.dicts as dicts
or
from xRedUtils import dicts
```
"""

import sys, json, io
sys.dont_write_bytecode = True
from typing import overload

from .type_hints import SIMPLE_ANY

__all__: tuple[str, ...] = (
    "dict_walk", "value_exist", "dict_merge", "flatten_dict", "json_to_dict", "dict_to_json"
)

@overload
def dict_walk(dictionary: dict[SIMPLE_ANY, SIMPLE_ANY], path: str | list[str], _sep: str = ".") -> SIMPLE_ANY: ...
@overload
def dict_walk(dictionary: dict[SIMPLE_ANY, SIMPLE_ANY], path: str | list[str], _sep: str = ".", _slice: slice = slice(None, None)) -> SIMPLE_ANY: ...

def dict_walk(dictionary: dict[SIMPLE_ANY, SIMPLE_ANY], path: str | list[str], _sep: str = ".", _slice: slice = slice(None, None)) -> SIMPLE_ANY:
    """
    Recursively walks through a dictionary to retrieve a value specified by a given path.

    ### Parameters:
    - `dictionary` - The dictionary to traverse.
    - `path` - The path to the desired value, specified as a `str` or `list of str`.

    - `_sep` - Separator used to split the path if it's a `str` (default is `"."`).
    - `_slice` - Slice object indicating the range of elements to consider in the path (default is `slice(None, None)` or full path).

    ### Returns:
    - The value found at the specified path within the dictionary.

    ### Raises:
    - `MemoryError` - If the specified path cannot be found within the dictionary.
    """
    current: dict[SIMPLE_ANY, SIMPLE_ANY] = dictionary
    path = path.split(_sep) if isinstance(path, str) else path

    for key in path[_slice]:
        if key in current:
            current = current[key]
        else:
            raise MemoryError(f"Failed to reach value specified: `{key}` on `{path}`")

    return current

def value_exist(dictionary: dict[SIMPLE_ANY, SIMPLE_ANY], path: str | list[str], **kwargs) -> bool:
    """
    Checks whether a value exists within a dictionary at the specified path.

    ### Parameters:
    - `dictionary` - The dictionary to search within.
    - `path` The path to the value being checked, specified as a `string` or `list of strings`.
    - `**kwargs` - Additional keyword arguments to pass to the `dicts.dict_walk` function.

    ### Returns:
    - `True` if the value exists at the specified path within the dictionary, `False` otherwise.
    """
    try:
        dict_walk(dictionary, path, **kwargs)
        return True 
    except:
        return False

def dict_merge(dict1, dict2) -> dict[SIMPLE_ANY, SIMPLE_ANY]:
    """
    Merges two dictionaries.

    ### Parameters:
    - `dict1` - The first dictionary to merge.
    - `dict2` - The second dictionary to merge.

    ### Returns:
    - A new `dictionary` containing the merged key-value pairs from both dictionaries.
    """
    return dict1 | dict2

@overload
def flatten_dict(dictionary: dict[str, SIMPLE_ANY], _sep: str= "_") -> dict[str, SIMPLE_ANY]: ...
@overload
def flatten_dict(dictionary: dict[str, SIMPLE_ANY], _sep: str= "_", _parent_key="") -> dict[str, SIMPLE_ANY]: ...

def flatten_dict(dictionary: dict[str, SIMPLE_ANY], _sep: str= "_", _parent_key="") -> dict[str, SIMPLE_ANY]:
    """
    Flattens a nested dictionary into a single-level dictionary.

    ### Parameters:
    - `dictionary` - The dictionary to flatten.
    - `_sep` - Separator used to join keys in the flattened dictionary (default is "_").
    - `_parent_key` - Internal parameter used for recursive calls to keep track of parent keys (default is `""`), can be changed, but will only be applied to the first level keys.

    ### Returns:
    - A single-level `dictionary` where nested keys are joined with the separator.
    """

    items: dict[str, SIMPLE_ANY] = {}
    
    for k, v in dictionary.items():
        new_key: str = f"{_parent_key}{_sep}{k}" if _parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, _sep=_sep, _parent_key=new_key).items())
        else:
            items[new_key] = v
    return items

def json_to_dict(d: bytes | str | bytearray | io.TextIOWrapper, **kwargs) -> dict[str, SIMPLE_ANY]:
    """
    Converts JSON data to a Python dictionary.

    ### Parameters:
    - `d` - JSON data, which can be provided as `bytes`, `string`, `bytearray`, or a `text file`.
    - `**kwargs` - Additional keyword arguments to pass to the `json.loads` function.

    ### Returns:
    - A `dictionary` containing the parsed JSON data.
    """
    if isinstance(d, io.TextIOWrapper):
        d = d.read()
    return json.loads(d, **kwargs)

def dict_to_json(dictionary: dict[SIMPLE_ANY, SIMPLE_ANY], indent: int = 4, **kwargs) -> str:
    """
    Converts a dictionary to a JSON string with optional indentation and additional keyword arguments.

    ### Parameters:
    - `dictionary` - The dictionary to convert to JSON.
    - `indent` - The number of spaces used for indentation (default is `4`).  *Made for better readablity of JSON, can be set to `None`*
    - `**kwargs` - Additional keyword arguments to pass to the `json.dumps` function.

    ### Returns:
    - A JSON string representing the dictionary.
    """
    return json.dumps(dictionary, indent=indent, **kwargs)
