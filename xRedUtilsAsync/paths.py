"""
This module provides async converting between different types of paths. Supported for ALL OS-es.

### Constants:
- `PATH_SEPERATORS` - A dictionary mapping OS and its default path seperator.
- `CURRENT_SEPERATOR` - Your current OS path seperator
- `CWD` - Absolute path of your CWD (Current Working Directory)

### Functions:
- `to_absolute` - Convert a relative path to an absolute path.
- `to_relative` - Saves any data to existing or not existing file provided by the path.
- `to_uri` - Convert a file path to a file URI.
- `from_uri` - Convert a file URI to a file path.
- `join_paths` - Join multiple path parts or paths into a single path.

### Usage:
```py
import xRedUtilsAsync.paths as paths
or
from xRedUtilsAsync import paths
```
"""

import sys, os, urllib.parse
sys.dont_write_bytecode = True
from pathlib import Path

from xRedUtilsAsync.type_hints import STR_ITERABLE

__all__: tuple[str, ...] = (
    "PATH_SEPERATORS", "CURRENT_SEPERATOR", "CWD",
    "to_absolute", "to_relative", "to_uri", "from_uri", "join_parts"
)

PATH_SEPERATORS: dict[str, str] = {
    "Windows": "\\",
    "Linux": "/",
    "MacOS": "/",
    "Python": "."
}
CURRENT_SEPERATOR: str = os.sep
CWD: str = os.getcwd()

async def to_absolute(relative_path: str) -> str:
    """
    Convert a relative path to an absolute path.
    
    ### Parameters:
    - `relative_path` - Relative path in your file system.

    ### Returns:
    - `String` of the absolute path.
    """
    return str(Path(relative_path).resolve())

async def to_relative(absolute_path: str, base_path: str = None) -> str:
    """
    Convert an absolute path to a relative path based on the base path. (supports `..` or back walking)
    
    ### Example:
    ```py
    >>> absolute = "/home/red/xRedUtils/paths.py"
    >>> base = "/home/red"
    >>> to_relative(absolute, base)
    xRedUtils/paths.py
    ```

    ### Parameters:
    - `absolute_path` - Full/Absolute path in your file system.
    - `base_path` -  Base path to determinate relative path (normally CWD - Current Working Directory), if not provided, uses CWD

    ### Returns:
    - `String` of the relative path
    """

    return str(Path(absolute_path).relative_to(base_path or CWD, walk_up=True))

async def to_uri(path: str) -> str:
    """
    Convert a file path to a file URI.
    
    ### Parameters:
    - `path` - Path in `string` can be absolute or relative.

    ### Returns:
    - `String` represented as URI
    """
    return Path(path).resolve().as_uri()

async def from_uri(uri: str) -> str:
    """
    Convert a file URI to a file path.

    ### Parameters:
    - `uri` - URI in `string`.

    ### Returns:
    - `String` represented as absolute path.
    """
    parsed_url: urllib.parse.ParseResult = urllib.parse.urlparse(uri)
    return os.path.abspath(os.path.join(parsed_url.netloc, parsed_url.path))

async def join_paths(paths: STR_ITERABLE) -> str:
    """
    Join multiple path parts or paths into a single path.

    ### Parameters:
    - `paths` - `String iterable` represnting parts of the path.
    
    ### Returns:
    - Joined `string` representing path.
    """
    return str(Path(*paths))