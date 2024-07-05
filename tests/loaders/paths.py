import sys, typing, platform
sys.dont_write_bytecode = True

import xRedUtils.paths as sync_paths
import xRedUtilsAsync.paths as async_paths

_SEP: str = sync_paths.CURRENT_SEPERATOR
OS: str = platform.system()

def tester(_async: bool) -> None:
    PATHS = async_paths if _async else sync_paths
    
    TESTS: dict[typing.Callable, dict] = {
        PATHS.join_paths: {
            "kwargs": {
                "paths": ("home", "red", "xRedUtils", "tests", "async_test.py")
            },
            "result": f"home{_SEP}red{_SEP}xRedUtils{_SEP}tests{_SEP}async_test.py"
        },
        PATHS.to_absolute: {
            "kwargs": {
                "relative_path": "/xRedUtils/paths.py"
            },
            "result": "*" # Cannot determine due to OS differences, file positions
        },
        PATHS.to_relative: {
            "kwargs": {
                "absolute_path": "/home/red/xRedUtils/paths.py",
                "base_path": "/home/red"
            },
            "result": f"xRedUtils{_SEP}paths.py"
        },
        PATHS.to_uri: {
            "kwargs": {
                "path": "/home/red/xRedUtils/paths.py"
            },
            "result": f"file:///{"C:" if  OS == "Windows" else ""}/home/red/xRedUtils/paths.py"
        },
        PATHS.from_uri: {
            "kwargs": {
                "uri": f"file:///home/red/xRedUtils/paths.py"
            },
            "result": f"{"C:" if  OS == "Windows" else ""}{_SEP}home{_SEP}red{_SEP}xRedUtils{_SEP}paths.py"
        },
    }
    return TESTS