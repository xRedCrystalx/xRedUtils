"""
This module provides async functions for working with dictionaries and JSON data.

### Functions:
- `dict_walk` - Recursively walks through a dictionary to retrieve a value specified by a given path.
- `value_exist` - Checks whether a value exists within a dictionary at the specified path.
- `dict_merge` - Merges two dictionaries.
- `flatten_dict` - Flattens a nested dictionary into a single-level dictionary.
- `json_to_dict` - Converts JSON data to a Python dictionary.
- `dict_to_json` - Converts a dictionary to a JSON string with optional indentation and additional keyword arguments.
- `get_value` - Gets value of specified key.
- `get_key` - Gets key of specified value.
- `isEmpty` - Checks if the `dict` is empty.

### Usage:
```py

import xRedUtilsAsync.dicts as dicts
or
from xRedUtilsAsync import dicts
```
"""

import sys, json, io
sys.dont_write_bytecode = True
from .annotations import Iterator, Hashable, Any, overload

__all__: tuple[str, ...] = (
    "dict_walk", "value_exist", "dict_merge", "flatten_dict", "json_to_dict", "dict_to_json", "get_value", "get_key", "isEmpty"
)

@overload
async def dict_walk(dictionary: dict[Hashable, Any], path: str | list[str], _sep: str = ".") -> Any: ...
@overload
async def dict_walk(dictionary: dict[Hashable, Any], path: str | list[str], _sep: str = ".", _slice: slice = slice(None, None)) -> Any: ...

async def dict_walk(dictionary: dict[Hashable, Any], path: str | list[str], _sep: str = ".", _slice: slice = slice(None, None)) -> Any:
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
    current: dict[Hashable, Any] = dictionary
    path = path.split(_sep) if isinstance(path, str) else path

    for key in path[_slice]:
        if key in current:
            current = current[key]
        else:
            raise MemoryError(f"Failed to reach value specified: `{key}` on `{path}`")

    return current

async def value_exist(dictionary: dict[Hashable, Any], path: str | list[str], **kwargs) -> bool:
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
        await dict_walk(dictionary, path, **kwargs)
        return True 
    except:
        return False

async def dict_merge(dict1, dict2) -> dict[Hashable, Any]:
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
async def flatten_dict(dictionary: dict[str, Any], _sep: str= "_") -> dict[str, Any]: ...
@overload
async def flatten_dict(dictionary: dict[str, Any], _sep: str= "_", _parent_key="") -> dict[str, Any]: ...

async def flatten_dict(dictionary: dict[str, Any], _sep: str= "_", _parent_key="") -> dict[str, Any]:
    """
    Flattens a nested dictionary into a single-level dictionary.

    ### Parameters:
    - `dictionary` - The dictionary to flatten.
    - `_sep` - Separator used to join keys in the flattened dictionary (default is "_").
    - `_parent_key` - Internal parameter used for recursive calls to keep track of parent keys (default is `""`), can be changed, but will only be applied to the first level keys.

    ### Returns:
    - A single-level `dictionary` where nested keys are joined with the separator.
    """

    items: dict[str, Any] = {}
    
    for k, v in dictionary.items():
        new_key: str = f"{_parent_key}{_sep}{k}" if _parent_key else k
        if isinstance(v, dict):
            flatten: dict[str, Any] = await flatten_dict(v, _sep=_sep, _parent_key=new_key)
            items.update(flatten.items())
        else:
            items[new_key] = v
    return items

async def json_to_dict(d: bytes | str | bytearray | io.TextIOWrapper, **kwargs) -> dict[str, Any]:
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

async def dict_to_json(dictionary: dict[str, Any], indent: int = 4, **kwargs) -> str:
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

async def get_value(dictionary: dict[Hashable, Any], key: Any) -> Any | None:  
    """
    Gets value of specified key.

    ### Parameters:
    - `dictionary` - The dictionary to search.
    - `key` - Key to be used for searching.

    ### Returns:
    - Value of the key or `None` if key does not exist in dictionary.  
    """
    return dictionary.get(key)

async def get_key(dictionary: dict[Hashable, Any], value: Any) -> Any | None:
    """
    Gets key of specified value.
    
    ## ! WARNING !
    This will find the first value in the dictionary. 
    
    ### Parameters:
    - `dictionary` - The dictionary to search.
    - `value` - Value to be used for searching.

    ### Returns:
    - Key of the value or `None` if value does not exist in dictionary.  
    """
    # iter on dict only returns keys, so no point in optimizing that
    values = tuple(dictionary.values())

    try:
        index: int = values.index(value)
        key_iterator: Iterator[Hashable] = iter(dictionary)

        # moves until index -1
        for _ in range(index):
            next(key_iterator)
        else:
            return next(key_iterator)
    except:
        return None

async def isEmpty(dictionary: dict[Hashable, Any]) -> bool:
    """
    Checks if the `dict` is empty.

    ### Parameters:
    - `dictionary` - The dictionary to check.

    ### Returns:
    - `True` if empty, otherwise `False`
    """
    # next() throws error if there is nothing in iter, optimized way
    try:
        next(iter(dictionary))
        return False
    except:
        return True
