"""
Main testing module
WIP
"""
import sys, typing
sys.dont_write_bytecode = True
from src.type_hints import *
from src.errors import *

import src.dicts as test_dict
import src.times as test_time

def main_test() -> None:
    checks = {}


def runner(func: typing.Callable, *args, **kwargs) -> bool:
    try:
        func(*args, **kwargs)
    except Exception as error:
        print(full_traceback())