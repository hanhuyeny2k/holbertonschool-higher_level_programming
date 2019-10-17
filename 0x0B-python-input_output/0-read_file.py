#!/bin/usr/python3
"""
    Reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Args:
        filename - text file passing through.
    Return:
        None.
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
