#!/bin/usr/python3
"""
Using def read_file(filename="")

to reads a text file (UTF8) and prints it to stdout:

"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
