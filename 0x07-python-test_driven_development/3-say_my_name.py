#!/usr/bin/python3
"""Defines say_my_name.

Args:
    param1(first_name): a string.
    param2(last_name): a string.

Returns:
    None.

"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>."""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
