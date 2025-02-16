"""
Main sync testing module
"""

import sys, traceback
sys.dont_write_bytecode = True
from xRedUtils.annotations import Any, FunctionType

def load_modules() -> list:
    from .loaders import (
        cache as test_cache,
        colors as test_colors,
        dates as test_dates,
        dicts as test_dicts,
        errors as test_errors,
        funcs as test_funcs,
        general as test_general,
        generators as test_generators,
        hashing as test_hashing,
        iterables as test_iterables,
        maths as test_maths,
        modules as test_modules,
        objects as test_objects,
        paths as test_paths,
        regexes as test_regexes,
        strings as test_strings,
        times as test_times,
        type_converters as test_tconverters
    )

    return [
        test_cache, test_colors, test_dates, test_dicts, test_errors, test_funcs, test_general, test_generators,
        test_hashing, test_iterables, test_maths, test_modules, test_objects, test_paths, test_regexes, test_strings,
        test_times, test_tconverters
    ]

def main_test() -> None:
    for module in load_modules() or []:
        
        if (custom := getattr(module, "sync_custom", None)):
            custom()
        
        if not (tester := getattr(module, "tester", None)):
            continue
            
        for func, data in (tester(False) or dict()).items():

            if not runner(func, result=data.get("result"), *data.get("args", []), **data.get("kwargs", {})):
                print(f"Failed to run: {func.__qualname__}")
                print("--------------------------------")
    else:
        print("All tests complete.")

def runner(f: FunctionType, result: Any, *args, **kwargs) -> bool:
    try:
        response: Any = f(*args, **kwargs) 
        
        if result == "*" or response == result:
            return True

        print(f"Got: {response}\nExpected: {result}")

    except Exception:
        traceback.print_exc()
    
    return False
