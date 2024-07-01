"""
This module provides functions for `"hot reloading"`.

# USE THESE MODULES WITH YOUR OWN RISK!

### Functions:
- `load_module` - Imports new python module (in sys.modules) in the current running instance.
- `unload_module` - Removes cached module (sys.modules) from the current running instance.
- `reload_module` - Reloads cached module (sys.modules) in the current running instance with new version.

### Usage:
```py
import xRedUtils.modules.reloader as reloader
or
from xRedUtils.modules import reloader
```
"""

import sys, importlib.util, types
sys.dont_write_bytecode = True

__all__: tuple[str, ...] = (
    "load_module", "unload_module", "reload_module"
)

def load_module(path: str) -> types.ModuleType:
    """
    Imports new python module (in sys.modules) in the current running instance.
    
    ## WARNING: Adding a module dynamically can result to errors, crashes, overwrites etc. if not used properly. USE WITH YOUR OWN RISK!
    
    ### Parameters:
    - `path` - Python like path of the module. (using `.` as seperators)

    ### Returns:
    - `ModuleType` (like `import x.y.z as r` > `r`) can be used to call module methods, classes, variables...
    """
    return importlib.import_module(path, None)

def unload_module(path: str) -> str | None:
    """
    Removes cached module (sys.modules) from the current running instance.
    
    ## WARNING: Removing a module dynamically can result to errors, crashes etc. if not used properly. USE WITH YOUR OWN RISK!
    
    ### Parameters:
    - `path` - Python like path of the module. (using `.` as seperators)

    ### Returns:
    - Python path, if successful else `None`.
    """
    if path in sys.modules:
        try:
            del sys.modules[path]
            return path
        except: pass

def reload_module(path: str, ignore_not_loaded: bool = False) -> types.ModuleType | None:
    """
    Reloads cached module (sys.modules) in the current running instance with new version.
    
    ## WARNING: Reloading a module dynamically can result to errors, crashes, overwrites etc. if not used properly. USE WITH YOUR OWN RISK!
    
    ### Parameters:
    - `path` - Python like path of the module. (using `.` as seperators)
    - `ignore_not_loaded` - 

    ### Returns:
    - `ModuleType` of reloaded version, if successful else `None`.
    """
    if not unload_module(path) and not ignore_not_loaded:
        raise ImportWarning("Module not loaded. Use `ignore_not_loaded = True` to bypass this warning or load the module using `load_module`")

    return load_module(path)
