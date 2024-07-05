import sys, typing
sys.dont_write_bytecode = True
from xRedUtils.type_hints import SIMPLE_ANY

import xRedUtils.iterables as sync_iterables
import xRedUtilsAsync.iterables as async_iterables

PRIMARY_ITERABLE: list[SIMPLE_ANY] = ["Yes", 5, [True, False, None, [True, True]], ["STR"], 2.123]

SECONDARY_ITERABLE: list[SIMPLE_ANY] = ["Yes", None, 124, None, True, False, id, None]

def tester(_async: bool) -> None:
    ITERABLES = async_iterables if _async else sync_iterables
    
    TESTS: dict[typing.Callable, dict] = {
        ITERABLES.flatten_iterable: {
            "kwargs": {
                "iterable": PRIMARY_ITERABLE
            },
            "result": ["Yes", 5, True, False, None, True, True, "STR", 2.123]
        },
        ITERABLES.remove_items: {
            "kwargs": {
                "iterable": SECONDARY_ITERABLE,
                "item": None
            },
            "result": ["Yes", 124, True, False, id]
        },
        ITERABLES.remove_type: {
            "kwargs": {
                "iterable": SECONDARY_ITERABLE,
                "obj": type(None)
            },
            "result": ["Yes", 124, True, False, id]
        },
        ITERABLES.compare_iterables: {
            "kwargs": {
                "iterable1": [None, True, id, 1, "1"],
                "iterable2": SECONDARY_ITERABLE
            },
            "result": [None, True, id, 1]
        },
        ITERABLES.count_occurrences: {
            "kwargs": {
                "iterable": SECONDARY_ITERABLE,
                "item": None
            },
            "result": 3
        },
        ITERABLES.get_attr_data: {
            "kwargs": {
                "iterable": [complex(10, 3), complex(523, 34), complex(12, 54)],
                "attr": "imag"
            },
            "result": [3, 34, 54]
        },
        ITERABLES.to_iterable : {
            "kwargs": {
                "data": "Hello World!",
                "slice": True
            },
            "result" : ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!"]
        }
    }
    return TESTS