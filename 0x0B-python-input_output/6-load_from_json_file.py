#!/usr/bin/python3
"""Define a load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file” """

    with open(filename, 'r') as f:
        r = f.read()
        return json.loads(r)
