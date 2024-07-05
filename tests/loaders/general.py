import sys, typing
sys.dont_write_bytecode = True

import xRedUtils.general as sync_general
import xRedUtilsAsync.general as async_general

def tester(_async: bool) -> None:
    GENERAL = async_general if _async else sync_general
    
    TESTS: dict[typing.Callable, dict] = {
        GENERAL.isPalindrome: {
            "kwargs": {
                "p": "12321"
            },
            "result": True
        },
        GENERAL.generate_uuid: {
            "result": "*" # cannot be determinated due to its generation
        }
    }
    return TESTS