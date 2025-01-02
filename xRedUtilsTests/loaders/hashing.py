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
    }
    return TESTS