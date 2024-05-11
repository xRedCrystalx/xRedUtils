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

def json_to_dict(d: bytes | str | bytearray | io.TextIOWrapper, **kwargs) -> dict[str, SIMPLE_ANY]:
    """
    Converts JSON data to a Python dictionary.

    ### Parameters:
    - `d` - JSON data, which can be provided as `bytes`, `str`, `bytearray`, or a `text file`.
    - `**kwargs` - Additional keyword arguments to pass to the `json.loads` function.

    ### Returns:
    - A Python dictionary containing the parsed JSON data.
    """
    if isinstance(d, io.TextIOWrapper):
        d = d.read()
    return json.loads(d, **kwargs)

def value_exist(dictionary: dict[SIMPLE_ANY, SIMPLE_ANY], path: str | list[str], **kwargs) -> bool:
    """
    Checks whether a value exists within a dictionary at the specified path.

    ### Parameters:
    - `dictionary` - The dictionary to search within.
    - `path` The path to the value being checked, specified as a `str` or `list of str`.
    - `**kwargs` - Additional keyword arguments to pass to the `dicts.dict_walk` function.

    ### Returns:
    - `True` if the value exists at the specified path within the dictionary, `False` otherwise.
    """
    try:
        dict_walk(dictionary, path, **kwargs)
        return True 
    except:
        return False