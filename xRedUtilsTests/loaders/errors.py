import sys, typing, json
sys.dont_write_bytecode = True

import xRedUtils.errors as sync_errors
import xRedUtilsAsync.errors as async_errors


def tester(_async: bool) -> None:
    ERRORS = async_errors if _async else sync_errors
    
    TESTS: dict[typing.Callable, dict] = {
        ERRORS.full_traceback: {
            "kwargs": {
                "error": TypeError("full_traceback tester")
            },
            "result": "TypeError: full_traceback tester\n"
        },
        ERRORS.simple_error: {
            "kwargs": {
                "error": TypeError("simple_error tester"),
            },
            "result": "TypeError: simple_error tester"
        }
    }
    return TESTS
