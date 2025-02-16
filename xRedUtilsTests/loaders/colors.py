import sys, typing, datetime
sys.dont_write_bytecode = True

import xRedUtils.colors as sync_colors
import xRedUtilsAsync.colors as async_colors

def tester(_async: bool) -> None:
    COLORS = async_colors if _async else sync_colors
    
    TESTS: dict[typing.Callable, dict] = {
        COLORS.rem_colors: {
            "kwargs": {
                "s": "\x1b[38;5;16mHi, this is test\x1b[0m"
            },
            "result": "Hi, this is test"
        },
        COLORS.rgb_to_ansi: {
            "kwargs": {
                "r": 242,
                "g": 1,
                "b": 15,
                "option": "bg"
            },
            "result": "\x1b[48;2;242;1;15m"
        }
    }
    return TESTS