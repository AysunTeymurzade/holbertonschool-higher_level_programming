#!/usr/bin/python3
"""
This module provides the add_integer function.
"""

def add_integer(a, b=98):
    """
    Adds two integers (or floats casted to integers).

    Args:
        a: First number (int or float).
        b: Second number (int or float), default is 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
