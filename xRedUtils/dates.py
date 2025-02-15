"""
This module provides datetime handlers.

### Functions:
- `get_datetime` - Get the current datetime.
- `timestamp` - Converts a datetime object to a UNIX timestamp.

### Usage:
```py

import xRedUtils.dates as dates
or
from xRedUtils import dates
```
"""

import sys, datetime, time
sys.dont_write_bytecode = True
from .annotations import Literal

__all__: tuple[str, ...] = (
    "get_datetime", "timestamp"
)

def get_datetime(option: Literal["UTC"] | None = None) -> datetime.datetime:
    """
    Get the current datetime.

    ### Parameters:
    - `option` - If `"UTC"` is provided, returns the current datetime in UTC timezone.
    ### Returns:
    - Current `datetime` object.
    """
    if option == "UTC":
        return datetime.datetime.now(datetime.UTC)

    return datetime.datetime.now()

def timestamp(dt: datetime.datetime = None) -> int:
    """
    Converts a datetime object to a UNIX timestamp.

    ### Parameters:
    - `dt` - Optional `datetime` object to convert, otherwise current timestamp will be returned.

    ### Returns:
    - The UNIX timestamp corresponding to the input datetime in `int`.
    """
    if dt and isinstance(dt, datetime.datetime):
        return int(dt.timestamp())
    
    return int(time.time())
