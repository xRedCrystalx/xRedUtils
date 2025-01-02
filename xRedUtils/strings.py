"""
This module provides string manipulation functions.

### Functions:
- `pluralize` - Pluralizes a given singular word.
- `singularize` - Singularize a given plural word.
- `string_split` - Splits a string into chunks of specified size.
- `levenshtein_distance` - Compute the Levenshtein distance between two strings.
- `hamming_distance` - Calculate the Hamming distance between two strings.
- `capitalize_words` - Split the `string` into words using split, capitalize each word using capitalize, and join the capitalized words using join.

### Usage:
```py

import xRedUtils.strings as strings
or
from xRedUtils import strings
```
"""

import sys, string
sys.dont_write_bytecode = True
from typing import Literal, overload

from .iterables import chunker

__all__: tuple[str, ...] = (
    "ASCII_LETTERS", "ASCII_LOWERCASE", "ASCII_UPPERCASE", "BINARY", "DIGITS", "HEXDIGITS", "OCTDIGITS", "PUNCTUATION", "WHITESPACES"
    "pluralize", "singularize", "string_split", "levenshtein_distance", "capitalize_words", "hamming_distance"
)

ASCII_LETTERS: str = string.ascii_letters
ASCII_LOWERCASE: str = string.ascii_lowercase
ASCII_UPPERCASE: str = string.ascii_uppercase

BINARY: str = "01"
DIGITS: str = string.digits
OCTDIGITS: str = string.octdigits
HEXDIGITS: str = string.hexdigits

PUNCTUATION: str = string.punctuation
WHITESPACES: str = string.whitespace

def pluralize(singular: str) -> str:
    """
    Pluralizes a given singular word. -- Cannot handle irregular words.

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

def singularize(plural: str) -> str:
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
def capitalize_words(s: str) -> str: ...

def capitalize_words(s: str | list, _sep: str = " ") -> str:
    """
    Split the `string` into words using split, capitalize each word using capitalize, and join the capitalized words using join.

    ### Parameters:
    - `s` - String or list of words to be capitalized.
    - `_sep` - The separator used for splitting and joining.

    ### Returns:
    - String, each word capitalized.
    """
    if isinstance(s, list | set | tuple | frozenset):
        s = _sep.join(s)
    
    return string.capwords(s, sep=_sep)

@overload
def string_split(s: str, chunk_size: int, option: Literal["normal", "smart"] = "normal") -> list[str]: ...
@overload
def string_split(s: str, chunk_size: int, option: Literal["normal", "smart"] = "normal", _sep: str = " ") -> list[str]: ...

def string_split(s: str, chunk_size: int, option: Literal["normal", "smart"] = "normal", _sep: str = " ") -> list[str]:
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
        for chunk in s.split(_sep):
            chunk_len: int = len(chunk) + len(_sep)

            if chunk_counter + chunk_len > chunk_size:
                smart_strings.append(_sep.join(chunk_list))
                chunk_list, chunk_counter = [], 0

            chunk_counter += chunk_len
            chunk_list.append(chunk)

        smart_strings.append(_sep.join(chunk_list))

        return smart_strings

    return chunker(s, chunk_size)

def levenshtein_distance(string1: str, string2: str) -> int:
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
        return levenshtein_distance(string2, string1)

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

def hamming_distance(str1: str, str2: str) -> int:
    """
    Calculate the Hamming distance between two strings.
    
    ### Parameters:
    - `str1` - First string.
    - `str2` - Second string.
    
    ### Returns:
    - Hamming distance (integer).
    
    ### Raises:
    - `ValueError` if strings aren't equal length.
    """
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length.")
    
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))
