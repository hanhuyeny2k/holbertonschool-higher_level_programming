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
    line = " "
    for e in text:
        line += e
        if e in ".?:":
            print(line.strip(" "), end="\n\n")
            line = ""
    print(line.strip(" "), end="")
