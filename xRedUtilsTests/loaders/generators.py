import sys, typing
sys.dont_write_bytecode = True

import xRedUtils.generators as sync_generators
import xRedUtilsAsync.generators as async_generators

def tester(_async: bool) -> None:
    GENERATORS = async_generators if _async else sync_generators
    
    TESTS: dict[typing.Callable, dict] = {
        GENERATORS.generate_string: {
            "kwargs": {
                "length": 7
            },
            "result": "*"
        },
        GENERATORS.generate_uuid: {
            "kwargs": {},
            "result": "*"
        }
    }
    return TESTS