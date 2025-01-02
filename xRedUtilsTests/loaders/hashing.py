import sys, typing
sys.dont_write_bytecode = True

import xRedUtils.hashing as sync_hashing
import xRedUtilsAsync.hashing as async_hashing

def tester(_async: bool) -> None:
    HASHING = async_hashing if _async else sync_hashing
    
    TESTS: dict[typing.Callable, dict] = {
        HASHING.random_hash: {
            "kwargs": {
                "algorithm": "md5",
                "length": 7
            },
            "result": "*"
        },
        HASHING.create_hash: {
            "kwargs": {
                "algorithm": "sha256",
                "data": "test",
                "salt": "a"
            },
            "result": b"D\x17\xa3\r\xc8\xc6\xb5?^.+\x90Q\x15\x93H\x03`\x17\xf9\x06\x1e\x8a\xce\x1f\x96j\x1a\xb5\x8f\xbe\xdd"
        },
        HASHING.file_hash: {
            "kwargs": {
                "algorithm": "sha256",
                "file_path_or_io": "./xRedutilsTests/file_test.txt"
            },
            "result": b"\x19\xbdV\x17\xb1\xd4\x88P\n\xa6\xea!\xfeF\\\xb1\x9eO}\x1b\xf4\xdb\xa3\xf9\xa5\xe3*\xc6d.%\xb7"
        }
    }
    return TESTS