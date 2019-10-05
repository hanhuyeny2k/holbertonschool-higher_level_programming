#!/usr/bin/python3
"""Defines text_indentation.

Args:
    param1(text): an array of string.

Returns:
    None.

"""


def text_indentation(text):
    """Prints a text with 2 new lines after each ".", "?", ":" character."""
    if type(text) != str:
        raise TypeError("text must be a string")
    for e in text:
        if e in ".?:":
            print(e)
            print()
        else:
            print(e, end="")
