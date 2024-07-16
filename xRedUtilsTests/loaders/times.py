import sys, typing
sys.dont_write_bytecode = True

import xRedUtils.times as sync_times
import xRedUtilsAsync.times as async_times

def tester(_async: bool) -> None:
    TIMES = async_times if _async else sync_times
    
    TESTS: dict[typing.Callable, dict] = {
        TIMES.convert_to_seconds: {
            "kwargs": {
                "value": 23195,
                "option": "month"
            },
            "result": 60121440000
        },
        TIMES.seconds_to_str: {
            "kwargs": {
                "seconds": 3482
            },
            "result": "58 minutes, 2 seconds",
        },
        TIMES.str_to_seconds: {
            "kwargs": {
                "time_string": "58 minutes, 2 seconds"
            },
            "result": 3482
        }
    }
    return TESTS