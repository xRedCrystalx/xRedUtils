"""
Module with compiled useful regexes

### Usage:
```py

import xRedUtilsAsync.regexes as regexes
or
from xRedUtilsAsync import regexes
```
"""

import sys, re
sys.dont_write_bytecode = True

ANSI_PATTERN: re.Pattern[str] = re.compile(r"(?:\x1B\[|\x9B)[0-?]*[ -\/]*[@-~]", re.IGNORECASE)
URL_PATTERN: re.Pattern[str] = re.compile(r"\bhttps?://\S+\b")
DATE_PATTERN: re.Pattern[str] = re.compile(r"\d{4}-\d{2}-\d{2}") #YYYY-MM-DD

IPv4_PATTERN: re.Pattern[str] = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
IPv6_PATTERN: re.Pattern[str] = re.compile(r"\b(?:\[?[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\]?\b")
MAC_ADDR_PATTERN: re.Pattern[str] = re.compile(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", re.IGNORECASE)
