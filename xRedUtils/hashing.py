"""
This module provides functions for working with dictionaries and JSON data.

### Constants:
- `AVAILABLE_ALGORITHMS` - `Set` containing all supported hashing algorithms.
- `_LIT_ALGO` - `typing.Literal` of AVAILABLE_ALGORITHMS (for typehinting only)

### Functions:
- `random_hash` - Generates a random hash.
- `create_hash` - Hashes specified data with or without salt.
- `file_hash` - Calculates file hash.

### Usage:
```py

import xRedUtils.hashing as hashing
or
from xRedUtils import hashing
```
"""

import sys, hashlib, io
sys.dont_write_bytecode = True
from typing import Literal, overload

from .generators import generate_string

__all__: tuple[str, ...] = (
    "random_hash", "create_hash", "file_hash"
)

AVAILABLE_ALGORITHMS: set[str] = hashlib.algorithms_guaranteed
_LIT_ALGO = Literal['blake2b', 'md5', 'sha1', 'sha3_384', 'sha512', 'sha3_256', 'shake_128', 'sha224', 'blake2s', 'sha256', 'shake_256', 'sha3_224', 'sha384', 'sha3_512']


def random_hash(algorithm: _LIT_ALGO, length: int = 16, _enc: str = "utf-8") -> bytes:
    """
    Generates a random hash.
    
    ### Parameters:
    - `algorithm` - Hashing algorithm.
    - `length` - Length of randomly generated string used as base for hashing.
    - `_enc` - Encoding used for encoding/decoding string.

    ### Returns:
    - `Bytes` presentation of hash. (use `.hex()` to convert it to hexstring)
    """

    return hashlib.new(algorithm, generate_string(length).encode(_enc)).digest()

def create_hash(algorithm: _LIT_ALGO, data: str | bytes, salt: str | int = "", _enc: str = "utf-8") -> bytes:
    """
    Hashes specified data with or without salt.
    
    ### Parameters:
    - `algorithm` - Hashing algorithm.
    - `data` - Data that will be hashed.
    - `salt` - Optional `string` or `int` (int will generate random string of that length) used to harden hash cracking.
    - `_enc` - Encoding used for encoding/decoding string.

    ### Returns:
    - `Bytes` presentation of hash. (use `.hex()` to convert it to hexstring)
    """

    if isinstance(salt, int):
        salt = generate_string(salt, digits=True, puncs=True)
    
    if isinstance(data, bytes):
        data = data.decode(_enc)

    return hashlib.new(algorithm, (str(data) + str(salt)).encode(_enc)).digest()

def file_hash(algorithm: _LIT_ALGO, file_path_or_io: str | io.BufferedReader) -> bytes:
    """
    Calculates file hash. (Can get slow if file is big!)
    
    ### Parameters:
    - `algorithm` - Hashing algorithm.
    - `file_path_or_io` - `io.BufferedReader` or path to file that will be hash checked

    ### Returns:
    - `Bytes` presentation of hash. (use `.hex()` to convert it to hexstring)
    """

    if isinstance(file_path_or_io, str):

        with open(file_path_or_io, "rb") as f:
            return hashlib.file_digest(f, algorithm).digest()
    
    return hashlib.file_digest(file_path_or_io, algorithm).digest()
    
