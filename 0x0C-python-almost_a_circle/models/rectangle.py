#!/usr/bin/python3
'''
    create the Rectangle class
'''


from models.base import Base


class Rectangle(Base):
    '''
        it manages/initializes the width, height
        and coordinate values(x, y)
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):

        """Set/get value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''
            Returning private attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            sets a private attribute
        '''

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """returns a private attribute (y)"""

        return self.__y

    @y.setter
    def y(self, value):
        '''
            sets the private attribute for (y)
        '''

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        '''
            Returns: the area value of the Rectangle instance.
        '''

        return self.__width * self.__height

    def display(self):
        '''
            prints in stdout the Rectangle instance with the character (#)
        '''

        for a in range(self.__y):
            print("")

        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("{}".format("#"), end="")
            print()

    def __str__(self):
        '''
            it overrides the __str__ method and
            returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        '''

        a = self.id
        b = self.__x
        c = self.__y
        d = self.__width
        e = self.__height

        return "[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e)

    def update(self, *args, **kwargs):
        '''Update rectangle class instance attributes
            it assigns an argument to each attribute via the *args and **kwargs
            NB: kwarg = "key word argument"
                args = normal arguments(all arguments in the bracket)
            Args:
                *args (tuple): list of arguements
                *kwargs (dict): key and values of attributes
            *args is the list of arguments:
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute        
        '''
        attrs = ["id", "width", "height", "x", "y"]
        index = 0

        if args is not None and len(args) > 0:
            for arg in args:
                if index < 5:
                    setattr(self, attrs[index], arg)
                    index += 1
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
            Returns: the dictionary representation of a Rectangle
        '''

        elem = ["id", "width", "height", "x", "y"]
        ans = {}

        for i in elem:
            ans[i] = getattr(self, i)

        return ans
