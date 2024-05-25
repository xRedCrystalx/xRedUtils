"""
## RedUtils Python Library
────────────────────────────────────────────────\n
Simple, general purpose functions in one place! 

### Usage:
```py
>>> import xRedUtils
>>> xRedUtils.main_test()
"All checks passed!"
```

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

import xRedUtils.dates as dates
import xRedUtils.dicts as dicts
import xRedUtils.errors as errors
import xRedUtils.funcs as functions
import xRedUtils.general as general
import xRedUtils.maths as maths
import xRedUtils.regexes as regex
import xRedUtils.iterables as iterables
import xRedUtils.times as time
import xRedUtils.type_hints as typehints
import xRedUtils.strings as strings

from xRedUtils.test.test import main_test

def check_py_version() -> None | SystemError:
    if sys.version_info < (3, 12):
        raise SystemError("Python 3.12 or higher required!")
check_py_version()
