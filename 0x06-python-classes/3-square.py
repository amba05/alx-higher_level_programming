#!/usr/bin/python3
"""Defines a square."""


class Square:
    """represent the square."""

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

    def area(self):
        """Finds area of a square.
        Returns:
        area of square
        """
        return self.__size * self.__size
