"""
This module provides async functions for manipulating with iterables.

### Functions:
- `flatten_iterable` - Flattens a iterable into a single level list.
- `remove_items` - Removes all occurrences of a specified item from the iterable.
- `remove_type` - Removes all items of a specified type from the iterable.
- `compare_iterables` - Compare two iterables and return a list of items that are present in both iterables.
- `count_occurrences` - Count the number of times a specific item occurs in an iterable.
- `get_attr_data` - Retrieves attribute data from each object in the iterable. If no attribute was found, ignores the `item`.
- `to_iterable` - Converts data into a list.

### Usage:
```py
import xRedUtilsAsync.iterables as iterables
or
from xRedUtilsAsync import iterables
```
"""

import sys
sys.dont_write_bytecode = True

from .type_hints import SIMPLE_ANY, ITERABLE

__all__: tuple[str, ...] = (
    "flatten_iterable", "remove_items", "remove_type", "compare_iterables", "count_occurrences", "get_attr_data", "to_iterable"
)

async def flatten_iterable(iterable: ITERABLE) -> list[SIMPLE_ANY]:
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
    - A `list` containing all the elements of the iterable in one level.

    """
    if not isinstance(iterable, ITERABLE):
        return iterable

    new: list[SIMPLE_ANY] = []
    for element in iterable:
        if isinstance(element, ITERABLE):
            elements: list[SIMPLE_ANY] = await flatten_iterable(element)
            new.extend(elements)
        else:
            new.append(element)
    return new

async def remove_items(iterable: ITERABLE, item: SIMPLE_ANY) -> list[SIMPLE_ANY]:
    """
    Removes all occurrences of a specified item from the iterable.
    
    ### Parameters:
    - `iterable` - The iterable from which to remove items.
    - `item` - The item to remove from the iterable.
    
    ### Returns:
    -  A new `list` with the specified item removed.
    """
    return [element for element in iterable if element != item]

async def remove_type(iterable: ITERABLE, obj: type) -> list[SIMPLE_ANY]:
    """
    Removes all items of a specified type from the iterable.
    
    ### Parameters:
    - `iterable` - The iterable from which to remove types.
    - `obj` - The type of items to remove from the iterable.
    
    ### Returns:
    - A new `list` with items of the specified type removed.
    """
    return [element for element in iterable if not isinstance(element, obj)]

async def compare_iterables(iterable1: ITERABLE, iterable2: ITERABLE) -> list[SIMPLE_ANY]:
    """
    Compare two iterables and return a list of items that are present in both iterables.
    
    ### Parameters:
    - `iterable1` - The first iterable to compare.
    - `iterable2` - The second iterable to compare.
    
    ### Returns:
    -  A `list` of items present in both iterables.
    """
    return [item for item in iterable1 if item in iterable2]

async def count_occurrences(iterable: ITERABLE, item: SIMPLE_ANY) -> int:
    """
    Count the number of times a specific item occurs in an iterable.

    ### Parameters:
    - `iterable` - The `iterable` to search through.
    - `item` - The item to count occurrences of within the iterable.

    ### Returns:
    - The number of times the item occurs in the iterable.
    """
    return len([element for element in iterable if element == item])

async def get_attr_data(iterable: ITERABLE, attr: str) -> list[SIMPLE_ANY]:
    """
    Retrieves attribute data from each object in the iterable. If no attribute was found, ignores the `item`.

    ### Parameters:
    - `iterable` - The `iterable` to search through.
    - `attr` - Name of the attribute.

    ### Returns:
    - `Iterable` of returned attribute data.
    """
    return [data if (data := getattr(item, attr, "_NO_ATTR")) != "_NO_ATTR" else item for item in iterable]

async def to_iterable(data: SIMPLE_ANY, slice: bool = False) -> list[SIMPLE_ANY]:
    """
    Converts data into a list.
    
    ### Parameters:
    - `data` - The data that will be converted.
    - `slice` - If the data will be sliced. For example string `"Hello"` ➜  `["H", "e", "l", "l", "o"]`.

    ### Returns:
    - Data converted into an `iterable`.
    """
    if isinstance(data, ITERABLE) or slice:
        return list(data)

    return [data]
