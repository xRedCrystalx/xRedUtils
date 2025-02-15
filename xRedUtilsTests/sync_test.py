"""
Main sync testing module
"""

import sys, traceback
sys.dont_write_bytecode = True
from xRedUtils.annotations import Any, FunctionType

def load_modules() -> list:
    from .loaders import (
        dicts as test_dicts,
        iterables as test_iterables,
        dates as test_dates,
        maths as test_maths,
        strings as test_strings,
        funcs as test_funcs,
        paths as test_paths,
        general as test_general,
        objects as test_objects,
        errors as test_errors,
        generators as test_generators,
        hashing as test_hashing,
        type_converters as test_tconverters
    )

    return [
        test_dicts, test_iterables, test_dates, test_maths, test_strings, test_funcs, test_paths,
        test_general, test_objects, test_errors, test_generators, test_hashing, test_tconverters
    ]

def main_test() -> None:
    for module in load_modules() or []:
        
        if (custom := getattr(module, "custom", None)):
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
