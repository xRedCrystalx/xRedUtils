import sys, typing
sys.dont_write_bytecode = True

import xRedUtils.funcs as sync_funcs
import xRedUtilsAsync.funcs as async_funcs

def tester(_async: bool) -> None:
    FUNCS = async_funcs if _async else sync_funcs
    
    TESTS: dict[typing.Callable, dict] = {
        FUNCS.safe_call: {
            "kwargs": {
                "func": list,
                "_error": "none"
            },
            "result": []
        }
    }
    return TESTS