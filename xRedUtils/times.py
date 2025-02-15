"""
This module provides functions for converting time values between different units and formats.

### Functions:
- `convert_to_seconds` - Converts a time value from a specified unit to seconds.
- `seconds_to_str` - Converts a time duration in seconds to a human-readable string format.
- `str_to_seconds` - Converts a human-readable time string to its equivalent duration in seconds.

### Usage:
```py

import xRedUtils.times as times
or
from xRedUtils import times
```
"""

import sys
sys.dont_write_bytecode = True
from .annotations import NUMBER, Literal
from .strings import pluralize, singularize
from .general import TIME_UNITS

__all__: tuple[str, ...] = (
    "convert_to_seconds", "seconds_to_str", "str_to_seconds"
)

OPTIONS = Literal["second", "minute", "hour", "day", "week", "month", "year", "decade", "century", "millenium"]

def convert_to_seconds(value: NUMBER, option: OPTIONS) -> NUMBER:
    """
    Converts a time value from a specified unit to seconds.

    ### Parameters:
    - `value` - The numeric value of the time.
    - `option` - The unit of time to convert from, specified as a string literal.

    ### Returns:
    - The equivalent time value in seconds as `NUMBER`.
    """
    if not (multiplicator := TIME_UNITS.get(option)):
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

    for unit in reversed(TIME_UNITS.keys()):
        if seconds >= TIME_UNITS.get(unit, 0):
            count, seconds = divmod(seconds, TIME_UNITS.get(unit, 1))
            components.append(f"{count} {pluralize(unit) if count != 1 else unit}")

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
        total_seconds += int(count) * TIME_UNITS.get(singularize(unit), 0)

    return total_seconds
