import sys, typing
sys.dont_write_bytecode = True

import xRedUtils.objects as sync_objects
import xRedUtilsAsync.objects as async_objects

class Test:
    TEST: str = "Test"
    def test() -> None: ...

def tester(_async: bool) -> None:
    OBJECTS = async_objects if _async else sync_objects
    
    TESTS: dict[typing.Callable, dict] = {
        OBJECTS.extract_attributes: {
            "kwargs": {
                "obj": (t := Test())
            },
            "result": {"TEST": "Test", "test": t.test}
        },
        OBJECTS.get_object_name: {
            "kwargs": {
                "obj": Test,
            },
            "result": "Test"
        },
        OBJECTS.get_object_module_path: {
            "kwargs": {
                "obj": Test().test
            },
            "result": "xRedUtilsTests.loaders.objects"
        },
        OBJECTS.get_full_object_path: {
            "kwargs": {
                "obj": Test()
            },
            "result": "xRedUtilsTests.loaders.objects.Test" 
        }
    }
    return TESTS