import sys, importlib.util, types
sys.dont_write_bytecode = True


def resolve_name(name: str, package: str = None) -> str:
    return importlib.util.resolve_name(name, package)

def load_module(name: str, package: str = None) -> types.ModuleType:
    return importlib.import_module(name, package)

def unload_module(name: str, package: str = None) -> str | None:
    """
    Removes cached module (sys.modules) from the current running instance.
    
    ## WARNING: Removing a module dynamically can result to errors, crashes etc. if not used properly. USE WITH YOUR OWN RISK!
    
    ### Parameters:
    - `name` - Python like path of the module. (using `.` as seperators)
    - `package` - 

    ### Returns:
    - Python path, if sucessful else `None`

    """
    path = resolve_name(name, package)
    if path in sys.modules:
        try:
            del sys.modules[path]
            return path
        except: pass

def reload_module(name: str, package: str = None, ignore_not_loaded: bool = False) -> types.ModuleType | None:
    # removing cached module from system
    if not unload_module(name, package) and not ignore_not_loaded:
        raise ImportWarning("Module not loaded. Use `ignore_not_loaded = True` to bypass this warning or load the module using `load_module`")

    return load_module(name, package)