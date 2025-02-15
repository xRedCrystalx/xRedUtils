"""
This module provides functions for manipulating with iterables.

### Functions:
- `flatten_iterable` - Flattens a iterable into a single level list.
- `remove_items` - Removes all occurrences of a specified item from the iterable.
- `remove_type` - Removes all items of a specified type from the iterable.
- `compare_iterables` - Compare two iterables and return a list of items that are present in both iterables.
- `count_occurrences` - Count the number of times a specific item occurs in an iterable.
- `get_attr_data` - Retrieves attribute data from each object in the iterable. If no attribute was found, ignores the `item`.
- `chunker` - Slice iterable into chunks of specified size.
- `to_iterable` - Converts data into a list.

### Usage:
```py

import xRedUtils.iterables as iterables
or
from xRedUtils import iterables
```
"""

import sys, itertools
sys.dont_write_bytecode = True
from .annotations import Any, ITERABLE
from .errors import VersionMismatchError

__all__: tuple[str, ...] = (
    "flatten_iterable", "remove_items", "remove_type", "compare_iterables", "count_occurrences", "get_attr_data", "chunker", "to_iterable"
)

def flatten_iterable(iterable: ITERABLE) -> list[Any]:
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

    new: list[Any] = list()
   
    for element in iterable:
        if isinstance(element, ITERABLE):
            new.extend(flatten_iterable(element))
        else:
            new.append(element)
    return new

def remove_items(iterable: ITERABLE, item: Any) -> list[Any]:
    """
    Removes all occurrences of a specified item from the iterable.
    
    ### Parameters:
    - `iterable` - The iterable from which to remove items.
    - `item` - The item to remove from the iterable.
    
    ### Returns:
    -  A new `list` with the specified item removed.
    """
    return [element for element in iterable if element != item]

def remove_type(iterable: ITERABLE, obj: type) -> list[Any]:
    """
    Removes all items of a specified type from the iterable.
    
    ### Parameters:
    - `iterable` - The iterable from which to remove types.
    - `obj` - The type of items to remove from the iterable.
    
    ### Returns:
    - A new `list` with items of the specified type removed.
    """
    return [element for element in iterable if not isinstance(element, obj)]

def compare_iterables(iterable1: ITERABLE, iterable2: ITERABLE) -> list[Any]:
    """
    Compare two iterables and return a list of items that are present in both iterables.
    
    ### Parameters:
    - `iterable1` - The first iterable to compare.
    - `iterable2` - The second iterable to compare.
    
    ### Returns:
    -  A `list` of items present in both iterables.
    """
    return [item for item in iterable1 if item in iterable2]

def count_occurrences(iterable: ITERABLE, item: Any) -> int:
    """
    Count the number of times a specific item occurs in an iterable.

    ### Parameters:
    - `iterable` - The `iterable` to search through.
    - `item` - The item to count occurrences of within the iterable.

    ### Returns:
    - The number of times the item occurs in the iterable.
    """
    return len([element for element in iterable if element == item])

def get_attr_data(iterable: ITERABLE, attr: str) -> list[Any]:
    """
    Retrieves attribute data from each object in the iterable. If no attribute was found, ignores the `item`.

    ### Parameters:
    - `iterable` - The `iterable` to search through.
    - `attr` - Name of the attribute.

    ### Returns:
    - `Iterable` of returned attribute data.
    """
    return [data if (data := getattr(item, attr, "_NO_ATTR")) != "_NO_ATTR" else item for item in iterable]

def chunker(iterable: ITERABLE, chunk_size: int, strict: bool = False) -> itertools.batched:
    """
    Slice `iterable` into chunks of specified size
    
    ### Parameters:
    - `iterable` - Iterable that will be chunked.
    - `chunk_size` - Size/num of elements in each chunk.
    - `strict` - If the final chunk can be shorter than `chunk_size`.

    ### Returns:
    - `batched` object ➜ iterable of tuples.

    ### Raises:
    - `TypeError` if the final chunk is shorter than `chunk_size`.
    - `VersionMismatchError` if 
    """
    if strict and sys.version_info < (3, 13):
        raise VersionMismatchError("Strict argument requires python 3.13+")

    elif strict:
        return itertools.batched(iterable, chunk_size, strict=strict)
    else:
        return itertools.batched(iterable, chunk_size)

def to_iterable(data: Any, slice: bool = False) -> list[Any]:
    """
    Converts data into a list.
    
    ### Parameters:
    - `data` - The data that will be converted.
    - `slice` - If the data will be sliced. For example string `"Hello"` ➜ `["H", "e", "l", "l", "o"]`.

    ### Returns:
    - Data converted into an `iterable`.
    """
    if isinstance(data, ITERABLE) or slice:
        return list(data)

    return [data]
