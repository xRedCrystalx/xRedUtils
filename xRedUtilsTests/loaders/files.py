import sys, typing, os, random
sys.dont_write_bytecode = True

import xRedUtils.files as sync_files
import xRedUtilsAsync.files as async_files

CWD: str = os.getcwd()
FILE: str = random.choice(list(filter(lambda path: os.path.isfile(f"{CWD}/{path}"), os.listdir(CWD))))

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