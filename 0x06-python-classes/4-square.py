#!/usr/bin/python3
"""Define a square."""


class Square:
    """Defines the square
    Args:
        size (int): size of the square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get/set size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Get/set area of the square"""
        return self.__size * self.__size
