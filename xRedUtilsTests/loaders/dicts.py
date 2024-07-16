import sys, typing, json
sys.dont_write_bytecode = True
from xRedUtils.type_hints import SIMPLE_ANY

import xRedUtils.dicts as sync_dicts
import xRedUtilsAsync.dicts as async_dicts

PRIMARY_DICT: dict[str, SIMPLE_ANY] = {
    "a": 1, 
    "b": {
        "b": 10, 
        "c": 30, 
        "h": {
            "l": True
        }
    }, 
    "q": "14"
}

SECONDARY_DICT: dict[str, SIMPLE_ANY] = {
    "a": 1, 
    "b": {
        "b": 10, 
        "c": 30
    }, 
    "q": "14"
}

def tester(_async: bool) -> None:
    DICTS = async_dicts if _async else sync_dicts
    
    TESTS: dict[typing.Callable, dict] = {
        DICTS.dict_merge: {
            "kwargs": {
                "dict1": PRIMARY_DICT,
                "dict2": SECONDARY_DICT
            },
            "result": {"a": 1, "b": {"b": 10, "c": 30}, "q": "14"}
        },
        DICTS.dict_to_json: {
            "kwargs": {
                "dictionary": PRIMARY_DICT,
                "indent": None
            },
            "result": '{"a": 1, "b": {"b": 10, "c": 30, "h": {"l": true}}, "q": "14"}'
        },
        DICTS.dict_walk: {
            "kwargs": {
                "dictionary": PRIMARY_DICT,
                "path": "b:h:l:$",
                "_sep": ":",
                "_slice": slice(None, -1)
            },
            "result": True
        },
        DICTS.value_exist: {
            "kwargs": {
                "dictionary": PRIMARY_DICT,
                "path": "a-d",
                "_sep": "-"
            },
            "result": False
        },
        DICTS.json_to_dict: {
            "kwargs": {
                "d": json.dumps(PRIMARY_DICT),
            },
            "result": PRIMARY_DICT
        },
        DICTS.flatten_dict: {
            "kwargs": {
                "dictionary": PRIMARY_DICT
            },
            "result": {'a': 1, 'b_b': 10, 'b_c': 30, 'b_h_l': True, 'q': '14'}
        }
    }
    return TESTS
