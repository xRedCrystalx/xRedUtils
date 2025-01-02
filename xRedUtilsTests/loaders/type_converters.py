import sys, typing
sys.dont_write_bytecode = True

import xRedUtils.type_converters as sync_tconverters
import xRedUtilsAsync.type_converters as async_tconverters

def tester(_async: bool) -> None:
    TCONVERTERS = async_tconverters if _async else sync_tconverters
    
    TESTS: dict[typing.Callable, dict] = {
        TCONVERTERS.to_str: {
            "kwargs": {
                "obj": 23195,
            },
            "result": "23195"
        },
        TCONVERTERS.to_int: {
            "kwargs": {
                "obj": "3482"
            },
            "result": 3482
        },
        TCONVERTERS.to_float: {
            "kwargs": {
                "obj": "12.4565"
            },
            "result": 12.4565
        },
        TCONVERTERS.to_bool: {
            "kwargs": {
                "obj": "3482"
            },
            "result": True
        },
        TCONVERTERS.to_tuple: {
            "kwargs": {
                "obj": ["one two three"]
            },
            "result": ("one two three", )
        },
        TCONVERTERS.to_list: {
            "kwargs": {
                "obj": ("one two three", )
            },
            "result": ["one two three"]
        },
        TCONVERTERS.to_dict: {
            "kwargs": {
                "obj": [["1", 2], ["3", 4], ["5", 6]]
            },
            "result": {"1" : 2, "3" : 4, "5" : 6}
        },
        TCONVERTERS.to_set: {
            "kwargs": {
                "obj": [1, 2, 4, 1]
            },
            "result": {1, 2, 4}
        },
        TCONVERTERS.to_frozen_set: {
            "kwargs": {
                "obj": [1, 2, 4, 1]
            },
            "result": frozenset([1,2,4])
        },
        TCONVERTERS.to_bytes: {
            "kwargs": {
                "obj": "str",
                "encoding": "utf-8"
            },
            "result": "str".encode("utf-8")
        },
        TCONVERTERS.to_byte_array: {
            "kwargs": {
                "obj": "str",
                "encoding": "utf-8"
            },
            "result": bytearray("str".encode("utf-8"))
        },
        TCONVERTERS.to_none: {
            "kwargs": {
                "obj": "something"
            },
            "result": None
        }
    }
    return TESTS