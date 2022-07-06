#!/usr/bin/python3
"""Defines a from_json_string function."""
import json


def from_json_string(my_str):

    """convert a json 0bject to normal object."""
    f = json.loads(my_str)
    return f
