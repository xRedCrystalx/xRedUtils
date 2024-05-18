"""
Main testing module
WIP
"""
import sys, typing
sys.dont_write_bytecode = True
from xRedUtils.type_hints import *
from xRedUtils.errors import *
from xRedUtils.regexes import *
from xRedUtils.general import *

import xRedUtils.dicts as test_dict
import xRedUtils.times as test_time
import xRedUtils.sequences as test_sequences
import xRedUtils.funcs as test_funcs
import xRedUtils.dates as test_dates
import xRedUtils.maths as test_maths

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
    },
    test_dict.flatten_dict: {
        "kwargs": {
            "dictionary": {"a": 1, "b": {"b": 10, "c": 30, "h": {"l": True}}, "q": "14"}
        },
        "result": {"a": 1, "b_b": 10, "b_c": 30, "b_h_l": True, "q": "14"}
    }, 
    
    test_time.convert_to_seconds: {
        "kwargs": {
            "value": 23195,
            "option": "month"
        },
        "result": 60121440000
    },
    test_time.seconds_to_str: {
        "kwargs": {
            "seconds": 3482
        },
        "result": "58 minutes, 2 seconds",
    },
    test_time.str_to_seconds: {
        "kwargs": {
            "time_string": "58 minutes, 2 seconds"
        },
        "result": 3482
    },
    
    test_sequences.flatten_sequence: {
        "kwargs": {
            "sequence": ["Yes", 5, [True, False, None, [True, True]], ["STR"], 2.123]
        },
        "result": ["Yes", 5, True, False, None, True, True, "STR", 2.123]
    },
    test_sequences.remove_items: {
        "kwargs": {
            "sequence": ["Yes", 5, True, False, None, True, True, "STR", 2.123],
            "item": True
        },
        "result": ["Yes", 5, False, None, "STR", 2.123]
    },
    test_sequences.remove_type: {
        "kwargs": {
            "sequence": ["Yes", 5, None, None, None, None, None, "STR", 2.123],
            "obj": type(None)
        },
        "result": ["Yes", 5, "STR", 2.123]
    },

    test_funcs.safe_call: {
        "kwargs": {
            "func": list,
            "_error": "full"
        },
        "result": []
    },

    test_dates.get_datetime: {
        "result": test_dates.datetime.datetime.now()
    },
    test_dates.timestamp: {
        "kwargs": {
            "dt": test_dates.datetime.datetime.now()
        },
        "result": int(test_dates.time.time())
    },

    test_maths.root: {
        "kwargs": {
            "value": 81,
            "n": 4
        },
        "result": 3
    },
    test_maths.percentage_difference: {
        "kwargs": {
            "num1": 100,
            "num2": 30,
            "_resp": "decimal"
        },
        "result": 0.7
    },
    test_maths.value_from_percentage: {
        "kwargs": {
            "total": 100,
            "percentage": 25
        },
        "result": 25
    }
}

def main_test() -> None:
    fails: int = 0
    for func, data in checks.items():
        if not runner(func, data["result"], *data.get("args", []), **data.get("kwargs", {})):
            print(f"Failed to run: {func.__qualname__}")
            fails += 1
    else:
        if not fails:
            print("All checks passed!")
        else:
            total: int = len(checks)
            print(f"Completed {total-fails}/{total}.")

def runner(_f: typing.Callable, result: SIMPLE_ANY, *args, **kwargs) -> bool:
    try:
        response: SIMPLE_ANY = _f(*args, **kwargs)
        if result == "*" or response == result:
            return True
        
        print(f"Got: {response}\nExpected: {result}")

    except Exception:
        print(full_traceback())
    return False

main_test()