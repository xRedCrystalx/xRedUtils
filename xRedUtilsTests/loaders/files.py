import sys, typing, os
sys.dont_write_bytecode = True

import xRedUtils.files as sync_files
import xRedUtilsAsync.files as async_files

CWD: str = os.getcwd()
FILE: str = "xRedUtilsTests/file_test.txt"

def tester(_async: bool) -> None:
    FILES = async_files if _async else sync_files
    
    TESTS: dict[typing.Callable, dict] = {
        FILES.open_file: {
            "kwargs": {
                "path": f"{CWD}/{FILE}",
                "encoding": None,
                "mode": "rb"
            },
            "result": "*"
        }
        # can't really test FILES.save_file
    }
    return TESTS