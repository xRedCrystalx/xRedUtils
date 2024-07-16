"""
System information variables.

### Usage:
```py

import xRedUtils.system as system
or
from xRedUtils import system
```
"""

import sys, os, platform
sys.dont_write_bytecode = True

# OS
OS: str = platform.system()
MAC_VERSION: tuple[str, tuple[str, str, str], str] = platform.mac_ver()
WIN_VERSION: tuple[str, str, str, str] = platform.win32_ver()
UNIX_VERSION: tuple[str, str] = platform.libc_ver()
JAVA_VERSION: tuple[str, str, tuple[str, str, str], tuple[str, str, str]] = platform.java_ver()

# python
PY_COMPILER: str = platform.python_compiler()
PY_BUILD: tuple[str, str] = platform.python_build()
PY_BRANCH: str = platform.python_branch()
PY_IMPLEMENTATION: str = platform.python_implementation()
PY_VERSION: tuple[str, str, str] = platform.python_version_tuple()
RECURSION_LIMIT: int = sys.getrecursionlimit()

# system
MACHINE_TYPE: str = platform.machine()
NODE: str = platform.node()
ARCHITECTURE: tuple[str, str] = platform.architecture()
PLATFORM: str = platform.platform()
DEVICE_ENCODING: str | None = os.device_encoding(1)
CPU_COUNT: int | None = os.cpu_count()
PROCESSOR_NAME: str = platform.processor()

# windows specific
if OS == "Windows":
    DRIVES: list[str] = os.listdrives()

    WIN_EDITION: str = platform.win32_edition()
    WIN_IOT: bool = platform.win32_is_iot()

# mac specific
if OS == "Darwin":
    pass
