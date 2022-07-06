#!/usr/bin/python3
"""Define a save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """saves an obj in a json file"""

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
