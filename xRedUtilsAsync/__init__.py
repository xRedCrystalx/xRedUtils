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
__version__ = "2.4.0"

def check_py_version() -> None | SystemError:
    if sys.version_info < (3, 12):
        raise SystemError("Python 3.12 or higher required!")

check_py_version()

import xRedUtilsAsync.annotations as annotations
import xRedUtilsAsync.cache as cache
import xRedUtilsAsync.colors as colors
import xRedUtilsAsync.dates as dates
import xRedUtilsAsync.dicts as dicts
import xRedUtilsAsync.errors as errors
import xRedUtilsAsync.files as files
import xRedUtilsAsync.funcs as funcs
import xRedUtilsAsync.general as general
import xRedUtilsAsync.generators as generators
import xRedUtilsAsync.hashing as hashing
import xRedUtilsAsync.iterables as iterables
import xRedUtilsAsync.maths as maths
import xRedUtilsAsync.modules as modules
import xRedUtils.objects as objects
import xRedUtilsAsync.paths as paths
import xRedUtilsAsync.regexes as regexes
import xRedUtilsAsync.strings as strings
import xRedUtilsAsync.system as system
import xRedUtilsAsync.times as time
import xRedUtilsAsync.type_converters as type_converters

from xRedUtilsTests.async_test import main_test

del sys