import sys, typing
sys.dont_write_bytecode = True

import xRedUtils.maths as sync_maths
import xRedUtilsAsync.maths as async_maths

def tester(_async: bool) -> None:
    MATHS = async_maths if _async else sync_maths
    
    TESTS: dict[typing.Callable, dict] = {
        MATHS.root: {
            "kwargs": {
                "value": 81,
                "n": 4
            },
            "result": 3
        },
        MATHS.percentage_difference: {
            "kwargs": {
                "num1": 100,
                "num2": 30,
                "_resp": "decimal"
            },
            "result": 0.7
        },
        MATHS.value_from_percentage: {
            "kwargs": {
                "total": 140,
                "percentage": 25
            },
            "result": 35
        },
    }
    return TESTS