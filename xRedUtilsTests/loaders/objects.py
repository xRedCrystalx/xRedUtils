import sys, typing
sys.dont_write_bytecode = True

import xRedUtils.objects as sync_objects
import xRedUtilsAsync.objects as async_objects

class Test:
    TEST: str = "Test"
    def test() -> None: ...

OBJ = Test()

def tester(_async: bool) -> None:
    OBJECTS = async_objects if _async else sync_objects
    
    TESTS: dict[typing.Callable, dict] = {
        OBJECTS.extract_attributes: {
            "kwargs": {
                "obj": OBJ
            },
            "result": {"TEST": "Test", "test": OBJ.test}
        },
        OBJECTS.get_object_name: {
            "kwargs": {
                "obj": Test,
            },
            "result": "Test"
        },
        OBJECTS.get_object_module_path: {
            "kwargs": {
                "obj": OBJ.test
            },
            "result": "xRedUtilsTests.loaders.objects"
        },
        OBJECTS.get_full_object_path: {
            "kwargs": {
                "obj": OBJ
            },
            "result": "xRedUtilsTests.loaders.objects.Test" 
        },
        OBJECTS.get_inheritance_layers: {
            "kwargs": {
                "obj": Test
            },
            "result": [Test, object]
        },
        OBJECTS.get_all_running_objects: {
            "kwargs": {
                "_type": Test
            },
            "result": [OBJ]
        }
    }
    return TESTS