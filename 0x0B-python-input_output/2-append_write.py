#!/usr/bin/python3
"""Defines an append_write function."""


def append_write(filename="", text=""):

    """appends texts to a file."""
    with open(filename, mode="a+", encoding="UTF-8") as f:
        return f.write(text)
