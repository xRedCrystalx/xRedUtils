import sys
sys.dont_write_bytecode = True
from typing import Callable

from xRedUtils.type_hints import SIMPLE_ANY

def resolve_path(path: str) -> str:
    return path.replace("\\", ".").replace("/", ".")


def reload_module(path: str, returns: list[str] | None) -> list[Callable] | None:
    path = resolve_path(path)
    
    # removing cached module from system
    if path in sys.modules:
        del sys.modules[path]

    # re-importing module
    try:
        exec(f"import {path}")
    except Exception as error:
        return print(f"Failed to reload {path}. {type(error).__name__}: {error}")
    
    # returning callables
    if returns:
        return [getattr(sys.modules[path], x) for x in returns]