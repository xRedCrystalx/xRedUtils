"""
## Asynchronous xRedUtils Python Library
────────────────────────────────────────────────\n
Simple, general purpose async functions in one place! 

### Usage:
```py
>>> import xRedUtilsAsync, asyncio
>>> asyncio.run(xRedUtilsAsync.main_test())
All tests complete.
```

:copyright: (c) 2024 by xRedCrystalx.
:license: MIT, see LICENSE for more details.
"""

import sys
sys.dont_write_bytecode = True

__title__ = "xRedUtilsAsync"
__author__ = "xRedCrystalx"
__license__ = "MIT"
__copyright__ = "Copyright 2024-present xRedCrystalx"
__version__ = "2.3.0"

def check_py_version() -> None | SystemError:
    if sys.version_info < (3, 12):
        raise SystemError("Python 3.12 or higher required!")

check_py_version()

import xRedUtilsAsync.dates as dates
import xRedUtilsAsync.dicts as dicts
import xRedUtilsAsync.errors as errors
import xRedUtilsAsync.funcs as functions
import xRedUtilsAsync.system as system
import xRedUtilsAsync.maths as maths
import xRedUtilsAsync.regexes as regex
import xRedUtilsAsync.iterables as iterables
import xRedUtilsAsync.times as time
import xRedUtilsAsync.type_hints as typehints
import xRedUtilsAsync.strings as strings
import xRedUtilsAsync.files as files
import xRedUtilsAsync.paths as paths
import xRedUtilsAsync.general as general
import xRedUtilsAsync.colors as colors
import xRedUtilsAsync.hashing as hashing
import xRedUtilsAsync.generators as generators
import xRedUtilsAsync.type_converters as type_converters


import xRedUtilsAsync.modules.reloader as reloader

from xRedUtilsTests.async_test import main_test

del sys