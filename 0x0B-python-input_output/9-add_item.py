#!/usr/bin/python3
"""
Use JSON to adds all arguments to a Python list, and then save them to a file

"""
import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        myList = load_from_json_file("add_item.json")
    except (FileNotFoundError, ValueError):
        myList = []
    myList += sys.argv[1:]
    save_to_json_file(myList, "add_item.json")
