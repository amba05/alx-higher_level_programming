#!/usr/bin/python3
"""
    Define a Rectangle class with width and height
"""


class Rectangle:
    """Representation of a Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a rectnagle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Set/get value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Set/get value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns area of a rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Returns a printable representation of the rectangle class.

            print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            for y in range(self.__width):
                rect.append("#")
            # append new line until the last value of height
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return a string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
