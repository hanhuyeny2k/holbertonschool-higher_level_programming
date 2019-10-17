#!/usr/bin/python3
"""
Using def read_lines(filename="", nb_lines=0)

to reads n lines of a text file (UTF8) and prints it to stdout

"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as myFile:
        if nb_lines <= 0 or nb_lines >= len(myFile.readlines()):
            for line in myFile:
                print(line, end="")
        else:
            counter = 0
            myFile.seek(0)
            for line in myFile:
                if counter == nb_lines:
                    break
                else:
                    counter += 1
                    print(line, end="")
