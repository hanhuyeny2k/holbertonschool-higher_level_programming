#!/usr/bin/python3
"""Defines print square.

Args:
    param1(size): the size length of the square.

Returns:
    None.

"""


def print_square(size):
    """Prints a square with the character #."""
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == float and size < 0:
        raise TypeError("size must be an integer")
    for e in range(0, size):
        for f in range(0, size):
            print("#", end="")
        print()
