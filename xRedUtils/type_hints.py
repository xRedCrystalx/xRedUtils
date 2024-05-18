"""
Most of the important typehints.

Use ANY, ITERABLE_OF_ANYTHING and DICT_OF_ANYTHING with your own risk. (It might slow down your computer and break InteliSense)

Recommended:
- SIMPLE_ANY

Commonly used:
- BUILTINS - all built-in types without iterables or mappings
- NUMBER - all numerical types
- BINARY - binary types - bytes, memoryviews etc.
- ITERABLE - all built-in types that can be iterated (in for loop)

Others:
- all built-in type iterables
- all iterables with built-in type dicts

- all built-in type dicts without iterables
- all dicts with built-in type iterables

Usage:
import xRedUtils.type_hints as type_hints
or
from xRedUtils import type_hints
"""

import sys
sys.dont_write_bytecode = True

# basic
NUMBER = int | float | complex
BINARY = bytes | bytearray | memoryview
BUILTINS = NUMBER | None | str | bool | Exception | slice | object | type
ITERABLE = list | tuple | set | frozenset | range | map | filter | zip

SIMPLE_ANY = NUMBER | BINARY | BUILTINS | ITERABLE | dict | None

# normal iterables with type
NUM_ITERABLE = list[NUMBER] | tuple[NUMBER, ...] | set[NUMBER] | frozenset[NUMBER]
STR_ITERABLE = list[str] | tuple[str, ...] | set[str] | frozenset[str]
BOOL_ITERABLE = list[bool] | tuple[bool, ...] | set[bool] | frozenset[bool]
NONE_ITERABLE = list[None] | tuple[None, ...] | set[None] | frozenset[None]
BYTE_ITERABLE = list[bytes] | tuple[bytes, ...] | set[bytes] | frozenset[bytes]
DICT_ITERABLE = list[dict] | tuple[dict, ...] | set[dict] | frozenset[dict]
ITERABLE_OF_ITERABLES = list[ITERABLE] | tuple[ITERABLE, ...] | set[ITERABLE] | frozenset[ITERABLE]
EXCEPT_ITERABLE = list[Exception] | tuple[Exception, ...] | set[Exception] | frozenset[Exception]
MEMORY_ITERABLE = list[memoryview] | tuple[memoryview, ...] | set[memoryview] | frozenset[memoryview]
SLICE_ITERABLE = list[slice] | tuple[slice, ...] | set[slice] | frozenset[slice]
OBJECT_ITERABLE = list[object] | tuple[object, ...] | set[object] | frozenset[object]
TYPE_ITERABLE = list[type] | tuple[type, ...] | set[type] | frozenset[type]
BINARY_ITERABLE = list[BINARY] | tuple[BINARY, ...] | set[BINARY] | frozenset[BINARY]
ITERABLE_OF_BUILTINS = list[BUILTINS] | tuple[BUILTINS, ...] | set[BUILTINS] | frozenset[BUILTINS]

# normal dict with type
STR_DICT = dict[str, str]
INT_DICT = dict[str, int]
FLOAT_DICT = dict[str, float]
COMPLEX_DICT = dict[str, complex]
NUMBER_DICT = dict[str, NUMBER]
BYTES_DICT = dict[str, bytes]
BYTEARRAY_DICT = dict[str, bytearray]
MEMORYVIEW_DICT = dict[str, memoryview]
BINARY_DICT = dict[str, BINARY]
NONE_DICT = dict[str, None]
BOOL_DICT = dict[str, bool]
EXCEPTION_DICT = dict[str, Exception]
SLICE_DICT = dict[str, slice]
OBJECT_DICT = dict[str, object]
DICT_OF_TYPES = dict[str, type]

# normal iterable with type dict
STR_DICT_ITERABLE = list[STR_DICT] | tuple[STR_DICT, ...] | set[STR_DICT] | frozenset[STR_DICT]
INT_DICT_ITERABLE = list[INT_DICT] | tuple[INT_DICT, ...] | set[INT_DICT] | frozenset[INT_DICT]
FLOAT_DICT_ITERABLE = list[FLOAT_DICT] | tuple[FLOAT_DICT, ...] | set[FLOAT_DICT] | frozenset[FLOAT_DICT]
COMPLEX_DICT_ITERABLE = list[COMPLEX_DICT] | tuple[COMPLEX_DICT, ...] | set[COMPLEX_DICT] | frozenset[COMPLEX_DICT]
NUMBER_DICT_ITERABLE = list[NUMBER_DICT] | tuple[NUMBER_DICT, ...] | set[NUMBER_DICT] | frozenset[NUMBER_DICT]
BYTES_DICT_ITERABLE = list[BYTES_DICT] | tuple[BYTES_DICT, ...] | set[BYTES_DICT] | frozenset[BYTES_DICT]
BYTEARRAY_DICT_ITERABLE = list[BYTEARRAY_DICT] | tuple[BYTEARRAY_DICT, ...] | set[BYTEARRAY_DICT] | frozenset[BYTEARRAY_DICT]
MEMORYVIEW_DICT_ITERABLE = list[MEMORYVIEW_DICT] | tuple[MEMORYVIEW_DICT, ...] | set[MEMORYVIEW_DICT] | frozenset[MEMORYVIEW_DICT]
BINARY_DICT_ITERABLE = list[BINARY_DICT] | tuple[BINARY_DICT, ...] | set[BINARY_DICT] | frozenset[BINARY_DICT]
NONE_DICT_ITERABLE = list[NONE_DICT] | tuple[NONE_DICT, ...] | set[NONE_DICT] | frozenset[NONE_DICT]
BOOL_DICT_ITERABLE = list[BOOL_DICT] | tuple[BOOL_DICT, ...] | set[BOOL_DICT] | frozenset[BOOL_DICT]
EXCEPTION_DICT_ITERABLE = list[EXCEPTION_DICT] | tuple[EXCEPTION_DICT, ...] | set[EXCEPTION_DICT] | frozenset[EXCEPTION_DICT]
SLICE_DICT_ITERABLE = list[SLICE_DICT] | tuple[SLICE_DICT, ...] | set[SLICE_DICT] | frozenset[SLICE_DICT]
OBJECT_DICT_ITERABLE = list[OBJECT_DICT] | tuple[OBJECT_DICT, ...] | set[OBJECT_DICT] | frozenset[OBJECT_DICT]
DICT_OF_TYPES_ITERABLE = list[DICT_OF_TYPES] | tuple[DICT_OF_TYPES, ...] | set[DICT_OF_TYPES] | frozenset[DICT_OF_TYPES]

# normal dict with type iterable
DICT_OF_ITERABLES = dict[str, ITERABLE]
NUM_ITERABLE_DICT = dict[str, NUM_ITERABLE]
STR_ITERABLE_DICT = dict[str, STR_ITERABLE]
BOOL_ITERABLE_DICT = dict[str, BOOL_ITERABLE]
NONE_ITERABLE_DICT = dict[str, NONE_ITERABLE]
BYTE_ITERABLE_DICT = dict[str, BYTE_ITERABLE]
DICT_ITERABLE_DICT = dict[str, DICT_ITERABLE]
DICT_OF_ITERABLE_ITERABLES = dict[str, ITERABLE_OF_ITERABLES]
EXCEPT_ITERABLE_DICT = dict[str, EXCEPT_ITERABLE]
MEMORY_ITERABLE_DICT = dict[str, MEMORY_ITERABLE]
SLICE_ITERABLE_DICT = dict[str, SLICE_ITERABLE]
OBJECT_ITERABLE_DICT = dict[str, OBJECT_ITERABLE]
TYPE_ITERABLE_DICT = dict[str, TYPE_ITERABLE]
BINARY_ITERABLE_DICT = dict[str, BINARY_ITERABLE]
DICT_OF_ITERABLE_BUILTINS = dict[str, ITERABLE_OF_BUILTINS]

ANY = (
    SIMPLE_ANY | 
    ITERABLE | NUM_ITERABLE | STR_ITERABLE | BOOL_ITERABLE | NONE_ITERABLE | BYTE_ITERABLE | DICT_ITERABLE | EXCEPT_ITERABLE | MEMORY_ITERABLE | SLICE_ITERABLE | OBJECT_ITERABLE | TYPE_ITERABLE | BINARY_ITERABLE | ITERABLE_OF_BUILTINS |
    STR_DICT | INT_DICT | FLOAT_DICT | COMPLEX_DICT | NUMBER_DICT | BYTES_DICT | BYTEARRAY_DICT | MEMORYVIEW_DICT | BINARY_DICT | NONE_DICT | BOOL_DICT | EXCEPTION_DICT | SLICE_DICT | OBJECT_DICT | DICT_OF_TYPES |
    DICT_OF_ITERABLES | NUM_ITERABLE_DICT | STR_ITERABLE_DICT | BOOL_ITERABLE_DICT | NONE_ITERABLE_DICT | BYTE_ITERABLE_DICT | DICT_ITERABLE_DICT | DICT_OF_ITERABLE_ITERABLES | EXCEPT_ITERABLE_DICT | MEMORY_ITERABLE_DICT | SLICE_ITERABLE_DICT | OBJECT_ITERABLE_DICT | TYPE_ITERABLE_DICT | BINARY_ITERABLE_DICT | ITERABLE_OF_BUILTINS |
    SLICE_DICT_ITERABLE | INT_DICT_ITERABLE | FLOAT_DICT_ITERABLE | COMPLEX_DICT_ITERABLE | NUMBER_DICT_ITERABLE | BYTES_DICT_ITERABLE | BYTEARRAY_DICT_ITERABLE | MEMORYVIEW_DICT_ITERABLE | BINARY_DICT_ITERABLE | NONE_DICT_ITERABLE | BOOL_DICT_ITERABLE | EXCEPTION_DICT_ITERABLE | SLICE_DICT_ITERABLE | OBJECT_DICT_ITERABLE | DICT_OF_TYPES_ITERABLE
    )

ITERABLE_OF_ANYTHING = list[ANY] | tuple[ANY, ...] | set[ANY] | frozenset[ANY]
DICT_OF_ANYTHING = dict[str, ANY]
