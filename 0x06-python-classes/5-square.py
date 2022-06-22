#!/usr/bin/python3
"""Defines the square"""


class Square:
    """Defines of the square"""

    def __init__(self, size=0):
        """initialize the square
        Args:
            size (int): size of square
        """
        self.size = size

    @property
    """Get/set size of the square"""
    def size(self):
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
        """return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("{}".format("#"), end="")
                print()
