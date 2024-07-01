"""
This module provides async string manipulation functions.

### Functions:
- `pluralize` - Pluralizes a given singular word.
- `singularize` - Singularize a given plural word.
- `string_split` - Splits a string into chunks of specified size.
- `levenshtein_distance` - Compute the Levenshtein distance between two strings.

### Usage:
```py
import xRedUtilsAsync.strings as strings
or
from xRedUtilsAsync import strings
```
"""

import sys
sys.dont_write_bytecode = True
from typing import Literal, overload

__all__: tuple[str, ...] = (
    "pluralize", "string_split", "levenshtein_distance"
)

async def pluralize(singular: str) -> str:
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

async def singularize(plural: str) -> str:
    """
    Singularize a given plural word. -- Cannot handle irregular words.
    
    ### Parameters:
    - `plural` - The plural word to be singularized.

    ### Returns:
    - The singular form of the word.
    """
    if plural.endswith("ies"):
        return plural[:-3] + "y"
    
    elif [ending for ending in ["ses", "xes", "zes", "ches", "shes"] if plural.endswith(ending)]:
        return plural[:-2]
    
    elif plural.endswith("s"):
        return plural[:-1]

    return plural

@overload
async def string_split(string: str, chunk_size: int, option: Literal["normal", "smart"] = "normal") -> list[str]: ...
@overload
async def string_split(string: str, chunk_size: int, option: Literal["normal", "smart"] = "normal", _sep: str = " ") -> list[str]: ...

async def string_split(string: str, chunk_size: int, option: Literal["normal", "smart"] = "normal", _sep: str = " ") -> list[str]:
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

async def levenshtein_distance(string1: str, string2: str) -> int:
    """
    Compute the Levenshtein distance between two strings.

    String metric - minimum number of single-character edits (insertions, deletions or substitutions) required to change one string into the other. 
    
    ### Parameters:
    - `string1` - First string
    - `string2` - Second string
    
    *longer string will be used to do checks

    ### Returns:
    -  The minimum `number` of changes.
    """
    # switch (first argument must be longer than second)
    if len(string1) < len(string2):
        return await levenshtein_distance(string2, string1)

    # if second string is empty, means len(string1) instertions
    if len(string2) == 0:
        return len(string1)

    previous_row: list[int] = range(len(string2) + 1)
    
    for index1, char1 in enumerate(string1):
        current_row: list[int] = [index1+1]

        for index2, char2 in enumerate(string2):
            insertions: int = previous_row[index2+1] + 1
            deletions: int = current_row[index2] + 1
            substitutions: int = previous_row[index2] + (char1 != char2)
            current_row.append(min(insertions, deletions, substitutions))
    
        previous_row: list[int] = current_row
    
    return previous_row[-1]
