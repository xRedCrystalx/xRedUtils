import sys, typing
sys.dont_write_bytecode = True

import xRedUtils.strings as sync_strings
import xRedUtilsAsync.strings as async_strings

def tester(_async: bool) -> None:
    STRINGS = async_strings if _async else sync_strings
    
    TESTS: dict[typing.Callable, dict] = {
        STRINGS.string_split: {
            "kwargs": {
                "s": "This is a sample string to be split every nth character intelligently.",
                "chunk_size": 20,
                "option": "smart"
            },
            "result": ['This is a sample', 'string to be split', 'every nth character', 'intelligently.']
        },
        STRINGS.pluralize: {
            "kwargs": {
                "singular": "ferrule"
            },
            "result": "ferrules"
        },
        STRINGS.singularize: {
            "kwargs": {
                "plural": "ferrules"
            },
            "result": "ferrule" 
        },
        STRINGS.capitalize_words: {
            "kwargs": {
                "s": "this is a crazy string"
            },
            "result": "This Is A Crazy String" 
        },
        STRINGS.levenshtein_distance: {
            "kwargs": {
                "str1": "ferrules de ne",
                "str2": "ferrule di ni" 
            },
            "result": 3
        },
        STRINGS.hamming_distance: {
            "kwargs": {
                "str1": "ferrules de ne",
                "str2": "ferrules di ni" 
            },
            "result": 2
        }
    }
    return TESTS