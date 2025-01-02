import sys, typing, datetime, time
sys.dont_write_bytecode = True

import xRedUtils.dates as sync_dates
import xRedUtilsAsync.dates as async_dates

def tester(_async: bool) -> None:
    DATES = async_dates if _async else sync_dates
    
    TESTS: dict[typing.Callable, dict] = {
        DATES.get_datetime: {
            "result": "*"
        },
        DATES.timestamp: {
            "kwargs": {
                "dt": datetime.datetime.now()
            },
            "result": int(time.time())
        }
    }
    return TESTS