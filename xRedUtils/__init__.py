"""
RedUtils Python Library
────────────────────────────────────────────────
Simple, general purpose functions in one place! 

Usage:

>>> import xRedUtils
>>> xRedUtils.main_test()
"All checks passed!"

:copyright: (c) 2024 by xRedCrystalx.
:license: MIT, see LICENSE for more details.
"""

import sys
sys.dont_write_bytecode = True

__title__ = "RedUtils"
__author__ = "xRedCrystalx"
__license__ = "MIT"
__copyright__ = "Copyright 2024-present xRedCrystalx"
__version__ = "0.0.1"

import dates, dicts, errors, funcs, general, maths, regexes, sequences, times, type_hints
from test.test import main_test

def check_py_version() -> None | SystemError:
    if sys.version_info < (3, 12):
        raise SystemError("Python 3.12 or higher required!")
check_py_version()
