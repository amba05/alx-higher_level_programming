#!/usr/bin/python3
'''
    creates a Square class that inherits
    from the Rectangle class
'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        initializes the size of the square
        NB: a Square is a Rectangle with the same width and height
            therefore the width and height from rectangle get initialized
            with one value (size)
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y)

    @property
    def size(self):
        '''
            returns the width of the square though its getter
        '''

        return self.width

    @size.setter
    def size(self, value):
        '''
            sets the width and height throught their setters (size)
        '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        '''
            it overrides the __str__ method and
            returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        '''

        a = self.id
        b = self.x
        c = self.y
        d = self.width
        e = self.height

        return "[Square] ({}) {}/{} - {}".format(a, b, c, d)

    def update(self, *args, **kwargs):
        '''
            it assigns an argument to each attribute via the *args and **kwargs
            NB: kwarg = "key word argument"
            args = normal arguments(all arguments in the bracket)
        '''

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

        except IndexError:
            pass

    def to_dictionary(self):
        '''
            Returns: the dictionary representation of a Rectangle
        '''

        elem = ["id", "size", "x", "y"]
        ans = {}

        for i in elem:
            ans[i] = getattr(self, i)

        return ans
