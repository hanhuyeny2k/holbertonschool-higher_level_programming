#!/usr/bin/python3
"""
    Reads a text file (UTF8) and prints it to stdout

    using read_file(filename="")
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    Args:
        filename(str): text file passing through.
    Return:
        None.
    """
    with open(filename, mode="r", encoding="UTF-8") as myFile:
        print(myFile.read(), end="")
