#!/usr/bin/python3
"""Class Defination"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square
        Args:
            size (int): size of the square
            position (tuple): position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not value[0] >= 0 | value[1] >= 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """returns area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                if self.__position[0] > 0:
                    for i in range(self.__position[0]):
                        print("{}".format(" "), end="")
                for i in range(self.__size):
                    print("{}".format("#"), end="")
                print()
