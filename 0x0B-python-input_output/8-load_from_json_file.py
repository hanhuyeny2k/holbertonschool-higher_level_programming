#!/usr/bin/python3
import json
"""
Use JSON module to creates an Object from a JSON file

"""


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, mode="r", encoding='utf-8') as myFile:
        return json.load(myFile)
