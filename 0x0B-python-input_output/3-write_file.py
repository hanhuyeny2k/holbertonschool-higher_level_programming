#!/usr/bin/python3
"""
Use def write_file(filename="", text="")

to write a string to a text file (UTF8)

and returns the number of characters written

"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)
       and returns the number of characters written"""
    with open(filename, mode="w", encoding="UTF-8") as myFile:
        return myFile.write(text)
