#!/usr/bin/python3
"""Defines add_integer.

Args:
    param1 (int): Accept a float or integer.
    param2 (int): Accept a float or integer.

Returns:
    Integer: Only return an integer.

"""


def add_integer(a, b=98):
    """Add 2 integers."""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
