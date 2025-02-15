"""
This module provides mathematics functions.

### Functions:
- `root` - Computes the n-th root of a given value.
- `percentage_difference` - Calculates the percentage difference between two numbers.
- `value_from_percentage` - Calculates the value corresponding to a given percentage of a total.
- `sma` - Calculate the Simple Moving Average (SMA).
- `ema` - Calculate the Exponential Moving Average (EMA).
- `isPrime` - Check if a number is prime.

### Usage:
```py

import xRedUtils.maths as maths
or
from xRedUtils import maths
```
"""

import sys
sys.dont_write_bytecode = True
from .annotations import NUMBER, Iterable, Literal
from .errors import InvalidRootError

__all__: tuple[str, ...] = (
    "root", "percentage_difference", "value_from_percentage", "sma", "ema", "isPrime"
)

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
    - The value as `float` that corresponds to the given percentage of the total.
    """
    return (percentage / 100) * total

def sma(data: Iterable[NUMBER], period: NUMBER) -> list[NUMBER]:
    """
    Calculate the Simple Moving Average (SMA).
    
    ### Parameters:
    - `data` - List of numerical values
    - `period` - Number of periods to calculate the SMA

    ### Returns:
    - `List` of SMA (numerical) values.

    ### Raises:
    - `ValueError` if `period > len(data)`
    """
    if len(data) < period:
        raise ValueError("Data length cannot be less than the SMA period.")
    
    return [sum( data[i:i+period] ) / period for i in range(len(data) - period + 1)]

def ema(data: Iterable[NUMBER], period: NUMBER) -> list[NUMBER]:
    """
    Calculate the Exponential Moving Average (EMA).
    
    ### Parameters:
    - `data` - List of numerical values
    - `period` - Number of periods to calculate the EMA

    ### Returns:
    - `List` of EMA (numerical) values.

    ### Raises:
    - `ValueError` if `period > len(data)`
    """
    if len(data) < period:
        raise ValueError("Data length cannot be less than the EMA period.")
    
    ema: list[NUMBER] = [ (sum(data[:period]) / period) ] # Initial SMA to be able to calculate EMA    
    multiplier: NUMBER = 2 / (period + 1)

    for i in range(period, len(data)):
        ema.append((data[i] - ema[-1]) * multiplier + ema[-1])
    return ema

def isPrime(n: NUMBER) -> bool:
    """
    Check if a number is prime.
    
    ### Parameters:
    - `n` - Integer to check.

    ### Returns:
    - Boolean if n is prime or not.
    """
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    
    if n <= 3:
        return True  # 2 and 3 are prime numbers
    
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate multiples of 2 and 3
    
    # Check divisors from 5 to sqrt(n), skipping even numbers
    for i in range(5, int(root(n, 2) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True
