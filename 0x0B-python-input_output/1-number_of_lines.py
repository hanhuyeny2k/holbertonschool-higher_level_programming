#!/usr/bin/python3
"""
Using def number_of_lines(filename="")

to returns the number of lines of a text file.

"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    with open(filename, encoding="utf-8") as myFile:
        return len(myFile.readlines())
