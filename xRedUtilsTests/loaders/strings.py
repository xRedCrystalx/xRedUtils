import sys, typing
sys.dont_write_bytecode = True

import xRedUtils.strings as sync_strings
import xRedUtilsAsync.strings as async_strings

def tester(_async: bool) -> None:
    STRINGS = async_strings if _async else sync_strings
    
    TESTS: dict[typing.Callable, dict] = {
        STRINGS.string_split: {
            "kwargs": {
                "string": "This is a sample string to be split every nth character intelligently.",
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
        }
    }
    return TESTS