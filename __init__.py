"""
RedUtils Python Library
────────────────────────────────────────────────
Simple, general purpose functions in one place! 

Usage:

>>> import red_utils
>>> red_utils.main_test()
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
__version__ = "0.0.0-a1"

from src import *
from . import test

def check_py_version() -> None | Exception:
    if sys.version_info < (3, 12):
        raise SystemError("Python 3.12 or higher required!")
check_py_version()

if False:
    test.main()

del sys, test
