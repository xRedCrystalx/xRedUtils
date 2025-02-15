import sys, typing
sys.dont_write_bytecode = True
import xRedUtils.maths as sync_maths
import xRedUtilsAsync.maths as async_maths

NUBERS: list[int] = [1, 6, 4, 7, 2, 5, 7, 3, 6, 7, 2, 5, 7, 3, 6, 7, 0, 2, 3, 6, 9, 1, 3, 2]

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
        MATHS.sma: {
            "kwargs": {
                "data": NUBERS,
                "period": 3
            },
            "result": [3.6666666666666665, 5.666666666666667, 4.333333333333333, 4.666666666666667, 4.666666666666667, 5.0, 5.333333333333333, 5.333333333333333, 5.0, 4.666666666666667, 4.666666666666667, 5.0, 5.333333333333333, 5.333333333333333, 4.333333333333333, 3.0, 1.6666666666666667, 3.6666666666666665, 6.0, 5.333333333333333, 4.333333333333333, 2.0]
        },
        MATHS.ema: {
            "kwargs": {
                "data": NUBERS,
                "period": 3
            },
            "result": [3.6666666666666665, 5.333333333333333, 3.6666666666666665, 4.333333333333333, 5.666666666666666, 4.333333333333333, 5.166666666666666, 6.083333333333333, 4.041666666666666, 4.520833333333333, 5.760416666666666, 4.380208333333333, 5.190104166666666, 6.095052083333333, 3.0475260416666665, 2.523763020833333, 2.7618815104166665, 4.380940755208333, 6.690470377604166, 3.845235188802083, 3.4226175944010415, 2.7113087972005205]
        },
        MATHS.isPrime: {
            "kwargs": {
                "n": 11
            },
            "result": True
        }
    }
    return TESTS