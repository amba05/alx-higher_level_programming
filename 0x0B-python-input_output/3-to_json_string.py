#!/usr/bin/python3
"""Defines a to_json_string function."""
import json


def to_json_string(my_obj):

    """converts an object to json format."""
    f = json.dumps(my_obj)
    return f
