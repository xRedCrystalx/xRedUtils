"""
This module provides utilities for manipulating with sequences.

Functions:
- flatten_sequence: Flattens a sequence into a single level list.
- remove_items: Removes all occurrences of a specified item from the sequence.
- remove_type: Removes all items of a specified type from the sequence.
- compare_sequences: Compare two sequences and return a list of items that are present in both sequences.

Usage:
import xRedUtils.sequences as sequences
or
from xRedUtils import sequences
"""

import sys
sys.dont_write_bytecode = True

from type_hints import SIMPLE_ANY, ITERABLE

def flatten_sequence(sequence: ITERABLE) -> list[SIMPLE_ANY]:
    """
    Flattens a sequence into a single level list.

    Aka. this:
    ```python
    >>> flatten_sequence([1, [2, 3], [[4, 5], 6]])
    [1, 2, 3, 4, 5, 6]
    ```

    ### Parameters:
    - `sequence` - Any sequence (`list`, `tuple`, `set`...)

    ### Returns:
    - A list containing all the elements of the sequence in one level.

    """
    if not isinstance(sequence, ITERABLE):
        return sequence

    new: list[SIMPLE_ANY] = []
    for item in sequence:
        if isinstance(item, ITERABLE):
            new.extend(flatten_sequence(item))
        else:
            new.append(item)
    return new

def remove_items(sequence: ITERABLE, item: SIMPLE_ANY) -> list[SIMPLE_ANY]:
    """
    Removes all occurrences of a specified item from the sequence.
    
    ### Parameters:
    - `sequence` - The sequence from which to remove items.
    - `item` - The item to remove from the sequence.
    
    ### Returns:
    -  A new list with the specified item removed.
    """
    return [x for x in sequence if x != item]

def remove_type(sequence: ITERABLE, obj: type) -> list[SIMPLE_ANY]:
    """
    Removes all items of a specified type from the sequence.
    
    ### Parameters:
    - `sequence` - The sequence from which to remove types.
    - `obj` - The type of items to remove from the sequence.
    
    ### Returns:
    - A new list with items of the specified type removed.
    """
    return [x for x in sequence if not isinstance(x, obj)]

def compare_sequences(sequence1: ITERABLE, sequence2: ITERABLE) -> list[SIMPLE_ANY]:
    """
    Compare two sequences and return a list of items that are present in both sequences.
    
    ### Parameters:
    - `sequence1` - The first sequence to compare.
    - `sequence2` - The second sequence to compare.
    
    ### Returns:
    -  A `list` of items present in both sequences.
    """
    return [item for item in sequence1 if item in sequence2]
