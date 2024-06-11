"""
This module provides string functions.

### Functions:
- `pluralize` - Pluralizes a given singular word.
- `string_split` - Splits a string into chunks of specified size.

### Usage:
```py
import xRedUtils.strings as strings
or
from xRedUtils import strings
```
"""

import sys
sys.dont_write_bytecode = True
from typing import Literal, overload

__all__ = (
    "pluralize", "string_split"
)

def pluralize(singular: str) -> str:
    """
    Pluralizes a given singular word. -- Cannot handle special words.

    ### Parameters:
    - `singular` - The singular word to be pluralized.

    ### Returns:
    - The plural form of the word.
    """
    if singular[-1] == "y" and singular[-2] not in "aeiou":
        return singular[:-1] + "ies"

    if singular.endswith("o"):
        return singular + "es"

    if [ending for ending in ["s", "x", "z", "ch", "sh"] if singular.endswith(ending)]:
        return singular + "es"

    return singular + "s"

@overload
def string_split(string: str, chunk_size: int, option: Literal["normal", "smart"] = "normal") -> list[str]: ...
@overload
def string_split(string: str, chunk_size: int, option: Literal["normal", "smart"] = "normal", _sep: str = " ") -> list[str]: ...

def string_split(string: str, chunk_size: int, option: Literal["normal", "smart"] = "normal", _sep: str = " ") -> list[str]:
    """
    Splits a string into chunks of specified size.

    - `normal` - splits every nth character, exactly.
    - `smart` - tries to find closest separator and cuts the string there. (useful for cutting real sentences)

    ```python
    >>> string = "This is a sample string to be split every nth character intelligently."
    >>> string_split(string, 20, "normal")
    ['This is a sample str', 'ing to be split ever', 'y nth character inte', 'lligently.']

    >>> string_split(string, 20, "smart")
    ['This is a sample', 'string to be split', 'every nth character', 'intelligently.']
    ```

    ### Parameters:
    - `string` - The input string to be split.
    - `chunk_size` - The size of each chunk.
    - `option` - The splitting option. Default is `normal`.
    - `_sep` - The separator used for splitting. Default is `" "` (space).

    ### Returns:
    -  A `list of strings`, each representing a chunk of the original string.
    """
    if chunk_size <= 0:
        raise ValueError("Chunk_size must be greater than 0.")

    if option == "smart":
        smart_strings: list[str] = []

        chunk_list, chunk_counter = [], 0
        for chunk in string.split(_sep):
            chunk_len: int = len(chunk) + len(_sep)

            if chunk_counter + chunk_len > chunk_size:
                smart_strings.append(_sep.join(chunk_list))
                chunk_list, chunk_counter = [], 0

            chunk_counter += chunk_len
            chunk_list.append(chunk)

        smart_strings.append(_sep.join(chunk_list))

        return smart_strings

    return [string[i:i + chunk_size] for i in range(0, len(string), chunk_size)]


#TODO: custom placeholder handler
