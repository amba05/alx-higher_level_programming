# python - Inheritance

## important note
Technically, every class we create uses inheritance. All Python classes are subclasses of the special class named object. This class provides very little in terms of data and behaviors (those behaviors it does provide are all double-underscore methods intended for internal use only), but it does allow Python to treat all objects in the same way.

If we don’t explicitly inherit from a different class, our classes will automatically inherit from object. However, we can openly state that our class derives from object using the following syntax:
`class MySubClass(object):
 pass`

## Method Resolution order(MRO)
Method Resolution Order (MRO) is the order in which methods should be inherited in the presence of multiple inheritance. You can view the MRO by using the __mro__ attribute.
E.G `Dog.__mro__`

- In essence in multiple inheritance, the Class attributes are first checked/called first, then the Parent classes from left to right, then the classes inherited in each parent class from left to right.

## Doc testing file
- use this command to test file `python -m doctest -v example.txt` or 
	`python -m doctest -v test/example.txt`
	**example.txt is the file name, /test/ is file location**
