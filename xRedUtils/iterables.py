"""
This module provides utilities for manipulating with iterables.

### Functions:
- `flatten_iterable` - Flattens a iterable into a single level list.
- `remove_items` - Removes all occurrences of a specified item from the iterable.
- `remove_type` - Removes all items of a specified type from the iterable.
- `compare_iterables` - Compare two iterables and return a list of items that are present in both iterables.
- `count_occurrences` - Count the number of times a specific item occurs in an iterable.

### Usage:
```py
import xRedUtils.iterables as iterables
or
from xRedUtils import iterables
```
"""

import sys
sys.dont_write_bytecode = True

from .type_hints import SIMPLE_ANY, ITERABLE

def flatten_iterable(iterable: ITERABLE) -> list[SIMPLE_ANY]:
    """
    Flattens a iterable into a single level list.

    Aka. this:
    ```python
    >>> flatten_iterable([1, [2, 3], [[4, 5], 6]])
    [1, 2, 3, 4, 5, 6]
    ```

    ### Parameters:
    - `iterable` - Any iterable (`list`, `tuple`, `set`...)

    ### Returns:
    - A list containing all the elements of the iterable in one level.

    """
    if not isinstance(iterable, ITERABLE):
        return iterable

    new: list[SIMPLE_ANY] = []
    for element in iterable:
        if isinstance(element, ITERABLE):
            new.extend(flatten_iterable(element))
        else:
            new.append(element)
    return new

def remove_items(iterable: ITERABLE, item: SIMPLE_ANY) -> list[SIMPLE_ANY]:
    """
    Removes all occurrences of a specified item from the iterable.
    
    ### Parameters:
    - `iterable` - The iterable from which to remove items.
    - `item` - The item to remove from the iterable.
    
    ### Returns:
    -  A new list with the specified item removed.
    """
    return [element for element in iterable if element != item]

def remove_type(iterable: ITERABLE, obj: type) -> list[SIMPLE_ANY]:
    """
    Removes all items of a specified type from the iterable.
    
    ### Parameters:
    - `iterable` - The iterable from which to remove types.
    - `obj` - The type of items to remove from the iterable.
    
    ### Returns:
    - A new list with items of the specified type removed.
    """
    return [element for element in iterable if not isinstance(element, obj)]

def compare_iterables(iterable1: ITERABLE, iterable2: ITERABLE) -> list[SIMPLE_ANY]:
    """
    Compare two iterables and return a list of items that are present in both iterables.
    
    ### Parameters:
    - `iterable1` - The first iterable to compare.
    - `iterable2` - The second iterable to compare.
    
    ### Returns:
    -  A `list` of items present in both iterables.
    """
    return [item for item in iterable1 if item in iterable2]

def count_occurrences(iterable: ITERABLE, item: SIMPLE_ANY) -> int:
    """
    Count the number of times a specific item occurs in an iterable.

    ### Parameters:
    - `iterable` - The `iterable` to search through.
    - `item` - The item to count occurrences of within the iterable.

    ### Returns:
    - The number of times the item occurs in the iterable.
    """
    return len([element for element in iterable if element == item])
