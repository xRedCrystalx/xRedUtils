"""
Main testing module
"""

import sys, typing
sys.dont_write_bytecode = True
from xRedUtils.type_hints import SIMPLE_ANY
from xRedUtils.errors import full_traceback
from xRedUtils.system import OS

import xRedUtils.dicts as test_dict
import xRedUtils.times as test_time
import xRedUtils.iterables as test_iterables
import xRedUtils.funcs as test_funcs
import xRedUtils.dates as test_dates
import xRedUtils.maths as test_maths
import xRedUtils.strings as test_strings
import xRedUtils.files as test_files
import xRedUtils.paths as test_paths

_sep: str = test_paths.CURRENT_SEPERATOR

checks: dict[typing.Callable, dict[str, SIMPLE_ANY], tuple[SIMPLE_ANY, ...], SIMPLE_ANY] = {
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
    
    test_iterables.flatten_iterable: {
        "kwargs": {
            "iterable": ["Yes", 5, [True, False, None, [True, True]], ["STR"], 2.123]
        },
        "result": ["Yes", 5, True, False, None, True, True, "STR", 2.123]
    },
    test_iterables.remove_items: {
        "kwargs": {
            "iterable": ["Yes", 5, True, False, None, True, True, "STR", 2.123],
            "item": True
        },
        "result": ["Yes", 5, False, None, "STR", 2.123]
    },
    test_iterables.remove_type: {
        "kwargs": {
            "iterable": ["Yes", 5, None, None, None, None, None, "STR", 2.123],
            "obj": type(None)
        },
        "result": ["Yes", 5, "STR", 2.123]
    },
    test_iterables.compare_iterables: {
        "kwargs": {
            "iterable1": ["1", 1934, False, id],
            "iterable2": [None, True, id, 1, "1"]
        },
        "result": ["1", id]
    },
    test_iterables.count_occurrences: {
        "kwargs": {
            "iterable": ["Yes", None, 124, None, True, False, id, None],
            "item": None
        },
        "result": 3
    },
    test_iterables.get_attr_data: {
        "kwargs": {
            "iterable": [complex(10, 3), complex(523, 34), complex(12, 54)],
            "attr": "imag"
        },
        "result": [3, 34, 54]
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
    },

    test_strings.string_split: {
        "kwargs": {
            "string": "This is a sample string to be split every nth character intelligently.",
            "chunk_size": 20,
            "option": "smart"
        },
        "result": ['This is a sample', 'string to be split', 'every nth character', 'intelligently.']
    },
    test_strings.pluralize: {
        "kwargs": {
            "singular": "ferrule"
        },
        "result": "ferrules"
    },

    test_files.open_file: {
        "kwargs": {
            "path": r"C:\Users\Red\Documents\Projects\xRedUtils\xRedUtils\errors.py",
            "encoding": None,
            "mode": "rb"
        },
        "result": "*"
    },

    test_paths.join_paths: {
        "args": ("home", "red", "xRedUtils", "tests", "test.py"),
        "result": f"home{_sep}red{_sep}xRedUtils{_sep}tests{_sep}test.py"
    },
    test_paths.to_absolute: {
        "kwargs": {
            "relative_path": "/xRedUtils/paths.py"
        },
        "result": "*" # Cannot determine due to OS differences, file positions
    },
    test_paths.to_relative: {
        "kwargs": {
            "absolute_path": "/home/red/xRedUtils/paths.py",
            "base_path": "/home/red"
        },
        "result": f"xRedUtils{_sep}paths.py"
    },
    test_paths.to_uri: {
        "kwargs": {
            "path": "/home/red/xRedUtils/paths.py"
        },
        "result": f"file:///{"C:" if  OS == "Windows" else ""}/home/red/xRedUtils/paths.py"
    },
    test_paths.from_uri: {
        "kwargs": {
            "uri": "file:///home/red/xRedUtils/paths.py"
        },
        "result": f"{"C:" if  OS == "Windows" else ""}{_sep}home{_sep}red{_sep}xRedUtils{_sep}paths.py"
    }
}

#TODO: tests for regexes, general, errors?

def main_test() -> None:
    fails: int = 0
    for func, data in checks.items():
        if not runner(func, data.get("result"), *data.get("args", []), **data.get("kwargs", {})):
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
