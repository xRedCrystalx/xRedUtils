"""
This module provides functions for converting time values between different units and formats.

### Functions:
- `convert_to_seconds` - Converts a time value from a specified unit to seconds.
- `seconds_to_str` - Converts a time duration in seconds to a human-readable string format.
- `str_to_seconds` - Converts a human-readable time string to its equivalent duration in seconds.

### Constants:
- `UNITS` - A dictionary mapping time units to their conversion factors in seconds.
- `OPTIONS` - Literal type containing valid time unit options for conversion.

### Usage:
```py
import xRedUtils.times as times
or
from xRedUtils import times
```
"""

import sys, typing
sys.dont_write_bytecode = True

from .type_hints import NUMBER_DICT, NUMBER

__all__ = (
    "UNITS", "OPTIONS",
    "convert_to_seconds", "seconds_to_str", "str_to_seconds"
)

UNITS: NUMBER_DICT = {
    "second": 1,
    "minute": 60,
    "hour": 3_600,
    "day": 86_400,
    "week": 604_800,
    "month": 2_592_000,          # 30 days
    "year": 31_536_000,          # actual 365 days
    "decade": 315_532_800,
    "century": 3_155_673_600,
    "millenium": 31_556_908_800
}
OPTIONS = typing.Literal["second", "minute", "hour", "day", "week", "month", "year", "decade", "century", "millenium"]

def convert_to_seconds(value: NUMBER, option: OPTIONS) -> NUMBER:
    """
    Converts a time value from a specified unit to seconds.

    ### Parameters:
    - `value` - The numeric value of the time.
    - `option` - The unit of time to convert from, specified as a string literal.

    ### Returns:
    - The equivalent time value in seconds as `NUMBER`.
    """
    if not (multiplicator := UNITS.get(option)):
        return 0
    return value * multiplicator

def seconds_to_str(seconds: int, _sep: str = ", ") -> str:
    """
    Converts a time duration in seconds to a human-readable string format.

    ### Parameters:
    - `seconds` - The time duration in seconds.
    - `_sep` - Separator used to join components of the time duration (default is `", "`).

    ### Returns:
    - A human-readable `string` representing the time duration.
    """
    components: list[str] = []

    for unit in reversed(UNITS.keys()):
        if seconds >= UNITS[unit]:
            count, seconds = divmod(seconds, UNITS[unit])
            components.append(f"{count} {unit}{"s" if count != 1 else ""}")

    return _sep.join(components) if components else "0 seconds"

def str_to_seconds(time_string: str, _sep: str = ", ") -> int:
    """
    Converts a human-readable time string to its equivalent duration in seconds.

    ### Parameters:
    - `time_string` - The human-readable time string.
    - `_sep` Separator used to split components of the time string (default is `", "`).

    ### Returns:
    - The equivalent time duration in seconds as `int`.
    """
    total_seconds = 0
    components: map[str] = map(str.strip, time_string.split(_sep) or ())

    for comp in components:
        count, unit = comp.split(" ") or (0, "second")
        total_seconds += int(count) * UNITS[unit.rstrip("s")]

    return total_seconds
