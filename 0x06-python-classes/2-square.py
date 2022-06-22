#!/usr/bin/python3
"""a class Square that defines a square:"""


class Square:
    """a class Square that represent a square:"""

    def __init__(self, size=0):
        """Initialize a square

        Args:
            size (int): size of the square
        """

        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
