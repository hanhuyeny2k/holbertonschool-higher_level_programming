#!/usr/bin/python3
import json
"""
Use json module to returns an object (Python data structure)

represented by a JSON string

"""


def from_json_string(my_str):
    """Returns an object (Python data structure)
       represented by a JSON string"""
    return json.loads(my_str)
