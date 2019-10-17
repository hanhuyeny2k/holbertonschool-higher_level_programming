#!/bin/usr/python3
"""
Args:
    param1(filename) - text file passing through.

Returns:
    None.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
