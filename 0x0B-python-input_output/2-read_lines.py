#!/usr/bin/python3
"""
Using def read_lines(filename="", nb_lines=0)

to reads n lines of a text file (UTF8) and prints it to stdout

"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as myFile:
        if nb_lines <= 0:
            print(myFile.read(), end="")
        else:
            counter = 0
            myList = myFile.readlines()
            for line in myList:
                if counter == nb_lines:
                    break
                else:
                    counter += 1
                    print(line, end="")
