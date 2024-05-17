"""
General system information variables

Usage:
import red_utils.general as general
or
from red_utils import general
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

# system
MACHINE_TYPE: str = platform.machine()
NODE: str = platform.node()
ARCHITECTURE: tuple[str, str] = platform.architecture()
PLATFORM: str = platform.platform()
DEVICE_ENCODING: str | None = os.device_encoding(1)

WIN_EDITION: str = platform.win32_edition()
WIN_IOT: bool = platform.win32_is_iot()

CPU_COUNT: int | None = os.cpu_count()
PROCESSOR_NAME: str = platform.processor()
DRIVES: list[str] = os.listdrives()

CWD: str = os.getcwd()
RECURSION_LIMIT: int = sys.getrecursionlimit()
