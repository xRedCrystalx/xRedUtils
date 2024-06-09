"""
This module provides functions for dealing with files. Opening, saving, decoding...

### Functions:
- `open_file` - Opens any existing file provided by the path.
- `save_file` - Saves any data to existing or not existing file provided by the path.

### Usage:
```py
import xRedUtils.files as files
or
from xRedUtils import files
```
"""

import sys, json
sys.dont_write_bytecode = True

from typing import overload, Literal
from .type_hints import SIMPLE_ANY
from .dicts import json_to_dict

@overload
def open_file(path: str, encoding: str = "utf-8", mode: Literal["r", "rb"] = "r", **kwargs) -> str: ...
@overload
def open_file(path: str, encoding: str = "utf-8", mode: Literal["r", "rb"] = "r", decoder: Literal["json"] | None = None, **kwargs) -> dict[str, SIMPLE_ANY]: ...

def open_file(path: str, encoding: str = "utf-8", mode: Literal["r", "rb"] = "r", decoder: Literal["json"] | None = None, **kwargs) -> dict[str, SIMPLE_ANY]:
    """
    Opens any existing file provided by the path.

    ### Parameters:
    - `path` - Path to the file.
    - `encoding` - Encoding used for decoding. (Set to `None` if opening in `rb` mode)
    - `mode` - File opening mode
    
    - `decoder` - Usage of decoder. For example `json` would return a `dict` object
    - `**kwargs` - Extra kwargs provided for `open` built-in function 

    ### Returns:
    - `String`, `bytes`, `dict`... depends of provided arguments.
    """
    with open(path, encoding=encoding, mode=mode, **kwargs) as file:
        if decoder == "json":
            return json_to_dict(file)

        return file.read()

@overload
def save_file(path: str, data: SIMPLE_ANY, mode: str = "w") -> None: ...
@overload
def save_file(path: str, data: SIMPLE_ANY, mode: str = "w", encoder: Literal["json"] | None = None, **kwargs) -> None: ...

def save_file(path: str, data: SIMPLE_ANY, mode: str = "w", encoder: Literal["json"] | None = None, **kwargs) -> None:
    """
    Saves any data to existing or not existing file provided by the path.

    ### Parameters:
    - `path` - Path to the file.
    - `data` - Data that you want to save.
    - `mode` - File writing mode.
    
    - `encoder` - Usage of encoder. For example `json` would convert `dict` to `string`.
    - `**kwargs` - Extra kwargs for `encoders` settings 

    ### Returns:
    - Nothing.
    """
    with open(path, mode=mode, ) as file:
        if encoder == "json":
            json.dump(data, file, **kwargs)
            return
 
        file.write(data)