#!/usr/bin/python3
"""Defines a read file function."""


def read_file(filename=""):

    """Read the file."""
    with open(filename, 'r', encoding="UTF-8") as f:
        print(f.read(), end="")
