"""
This module provides async functions for modules.

# USE THESE MODULES WITH YOUR OWN RISK!

### Functions:
- `load_module` - Imports new python module (in sys.modules) in the current running instance.
- `unload_module` - Removes cached module (sys.modules) from the current running instance.
- `reload_module` - Reloads cached module (sys.modules) in the current running instance with new version.
- `get_types_of_module` - Finds all types (classes) in the module.

### Usage:
```py
import xRedUtilsAsync.modules as modules
or
from xRedUtilsAsync import modules
```
"""

import sys, importlib.util
sys.dont_write_bytecode = True
from .annotations import ModuleType

__all__: tuple[str, ...] = (
    "load_module", "unload_module", "reload_module", "get_types_of_module"
)

async def get_types_of_module(module: ModuleType, include_imports: bool = False) -> list[type]:
    """
    Finds all types (classes) in the module.

    ### Parameters:
    - `module` - Module to search in.
    - `include_imports` - If it should include all imported types.

    ### Returns:
    - Full python path of the object.
    """

    if include_imports:
        return [t for t in module.__dict__.values() if isinstance(t, type)]
    
    return [t for t in module.__dict__.values() if isinstance(t, type) and t.__module__ == module.__name__] # checks if same module - not import

async def load_module(path: str) -> ModuleType:
    """
    Imports new python module (in sys.modules) in the current running instance.
    
    ## WARNING: Adding a module dynamically can result to errors, crashes, overwrites etc. if not used properly. USE WITH YOUR OWN RISK!
    
    ### Parameters:
    - `path` - Python like path of the module. (using `.` as seperators)

    ### Returns:
    - `ModuleType` (like `import x.y.z as r` > `r`) can be used to call module methods, classes, variables...
    """
    return importlib.import_module(path, None)

async def unload_module(path: str) -> str | None:
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

async def reload_module(path: str, ignore_not_loaded: bool = False) -> ModuleType | None:
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
