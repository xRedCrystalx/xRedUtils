"""
This module provides functions for working with dictionaries and JSON data.

These functions are useful for navigating and manipulating dictionary-like data structures, especially when dealing with nested structures or JSON data.
"""

import sys, json, io
sys.dont_write_bytecode = True

from .type_hints import SIMPLE_ANY

def dict_walk(dictionary: dict[SIMPLE_ANY, SIMPLE_ANY], path: str | list[str], _sep: str = ".", _slice: slice = slice(None, None)) -> dict[SIMPLE_ANY, SIMPLE_ANY]:
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


def json_to_dict(d: bytes | str | bytearray | io.TextIOWrapper, **kwargs) -> dict[str, SIMPLE_ANY]:
    """
    Converts JSON data to a Python dictionary.

    ### Parameters:
    - `d` - JSON data, which can be provided as `bytes`, `string`, `bytearray`, or a `text file`.
    - `**kwargs` - Additional keyword arguments to pass to the `json.loads` function.

    ### Returns:
    - A Python dictionary containing the parsed JSON data.
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
