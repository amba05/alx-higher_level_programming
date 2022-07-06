#!/usr/bin/python3
"""Defines a write file function."""


def write_file(filename="", text=""):

    """write the text into a file."""
    with open(filename, mode="w", encoding='UTF-8') as f:
        return f.write(text)
