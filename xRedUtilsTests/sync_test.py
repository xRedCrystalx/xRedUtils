"""
Main sync testing module
"""

import sys, typing, traceback
sys.dont_write_bytecode = True

def load_modules() -> list:
    from .loaders import (
        dicts as test_dicts,
        iterables as test_iterables,
        dates as test_dates,
        maths as test_maths,
        strings as test_strings,
        files as test_files,
        funcs as test_funcs,
        paths as test_paths,
        general as test_general,
        objects as test_objects
    )

    return [test_dicts, test_iterables, test_dates, test_maths, test_strings, test_files, test_funcs, test_paths, test_general, test_objects]

def main_test() -> None:
    for module in load_modules() or []:
        if not (tester := getattr(module, "tester", None)):
            continue

        if tests := tester(False):
            for func, data in tests.items():
                if not runner(func, result=data.get("result"), *data.get("args", []), **data.get("kwargs", {})):
                    print(f"Failed to run: {func.__qualname__}")
    else:
        print("All tests complete.")

def runner(f: typing.Callable, result: typing.Any, *args, **kwargs) -> bool:
    try:
        response: typing.Any = f(*args, **kwargs) 
        
        if result == "*" or response == result:
            return True

        print(f"Got: {response}\nExpected: {result}")

    except Exception:
        traceback.print_exc()
    return False

#TODO: tests for regexes, general, errors?