#!/usr/bin/python3
import json
"""
Using a JSON representation to write an Object to a text file

"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, mode='w', encoding='utf-8') as myFile:
        return json.dump(my_obj, myFile)
