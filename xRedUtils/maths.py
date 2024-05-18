"""
This module provides mathematics functions.

Functions:
- root: Computes the n-th root of a given value.
- percentage_difference: Calculates the percentage difference between two numbers.
- value_from_percentage: Calculates the value corresponding to a given percentage of a total.

Usage:
import xRedUtils.maths as maths
or
from xRedUtils import maths
"""

import sys
sys.dont_write_bytecode = True
from typing import Literal

from .type_hints import NUMBER
from .errors import InvalidRootError

def root(value: NUMBER, n: int) -> NUMBER:
    """
    Computes the n-th root of a given value.

    ### Parameters:
    - `value` - The number to find the root of.
    - `n` - The degree of the root.

    ### Returns:
    - The n-th root of the value.

    ### Raises:
    - `InvalidRootError` - If value is negative and `n` is even, since the even root of a negative number is not a real number.
    """
    if value < 0 and n % 2 == 0:
        raise InvalidRootError("Cannot compute the even root of a negative number.")
    return value ** (1 / n)

def percentage_difference(num1: NUMBER, num2: NUMBER, _resp: Literal["decimal", "percent"] = "percent") -> NUMBER:
    """
    Calculates the percentage difference between two numbers.

    ### Parameters:
    - `num1` - The first number.
    - `num2` - The second number.
    - `_resp` - The format of the result. Can be "percent" or "decimal". Default is `percent`.

    ### Returns:
    - The percentage difference between the two numbers, in the specified format.

    ### Raises:
    - `ValueError` - If the biggest number is zero.
    """
    smaller, bigger = (num1, num2) if num2 > num1 else (num2, num1)

    if bigger == 0:
        raise ValueError("Biggest number cannot be 0!")

    value: float = (bigger - smaller) / bigger
    return value * 100 if _resp == "percent" else value

def value_from_percentage(total: NUMBER, percentage: NUMBER) -> NUMBER:
    """
    Calculates the value corresponding to a given percentage of a total.

    ### Parameters:
    - `total` - The total or whole amount.
    - `percentage` - The percentage of the total.

    ### Returns:
    - The value that corresponds to the given percentage of the total.
    """
    return (percentage / 100) * total
