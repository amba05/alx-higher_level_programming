#!/usr/bin/python3
""" Define add_interger module """


def add_integer(a, b=98):
    """
    Implement the add_interger module
    args:
        a (int)
        b (int)
    """

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')

    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    val_1 = int(a)
    val_2 = int(b)

    return val_1 + val_2
