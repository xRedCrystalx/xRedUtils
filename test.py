"""
Main testing module
WIP
"""
import sys, typing
sys.dont_write_bytecode = True
from src.type_hints import *
from src.errors import *

import src.dicts as test_dict
import src.times as test_time

checks: dict[typing.Callable, dict[str, SIMPLE_ANY]] = {
    test_dict.dict_merge: {
        "kwargs": {
            "dict1": {"a": 1, "b": {"b": 10, "c": 15}},
            "dict2": {"b": {"c": 30}, "q": "14"}
        },
        "result": {"a": 1, "b": {"c": 30}, "q": "14"}
    },
    test_dict.dict_to_json: {
        "kwargs": {
            "dictionary": {"a": 1, "b": {"b": 10, "c": 30}, "q": "14"},
            "indent": None
        },
        "result": '{"a": 1, "b": {"b": 10, "c": 30}, "q": "14"}'
    },
    test_dict.dict_walk: {
        "kwargs": {
            "dictionary": {"a": 1, "b": {"b": 10, "c": {"h": 9999}}, "q": "14"},
            "path": "b:c:h:$",
            "_sep": ":",
            "_slice": slice(None, 3)
        },
        "result": 9999
    },
    test_dict.value_exist: {
        "kwargs": {
            "dictionary": {"a": 1, "b": {"b": 10, "c": 15}},
            "path": "a.d"
        },
        "result": False
    },
    test_dict.json_to_dict: {
        "kwargs": {
            "d": '{"a": 1, "b": {"b": 10, "c": 30}, "q": "14"}',
        },
        "result": {"a": 1, "b": {"b": 10, "c": 30}, "q": "14"}
    }
}

def main_test() -> None:
    fails: int = 0
    for func, data in checks.items():
        if not data.get("args"):
            data["args"] = ()
        
        if not data.get("kwargs"):
            data["kwargs"] = {}

        if not runner(func, data["result"], *data["args"], **data["kwargs"]):
            print(f"Failed to run: {func.__qualname__}")
            fails += 1
    else:
        total: int = len(checks)
        print(f"Completed {total-fails}/{total}.")

def runner(func: typing.Callable, result: SIMPLE_ANY, *args, **kwargs) -> bool:
    try:
        response: SIMPLE_ANY = func(*args, **kwargs)
        if response == result:
            return True
        
        print(f"Got: {response}\nExpected: {result}")

    except Exception as error:
        print(full_traceback())
    return False
