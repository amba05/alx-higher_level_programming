# Python - Almost a circle

## Background Context
The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:

- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

You will also learn about:

- args and kwargs
- Serialization/Deserialization
- JSON

## Resources
**Read or watch:**

[args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
[JSON encoder and decoder](https://docs.python.org/3/library/json.html)
[unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
[Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

### Scripts to test documentation
- All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should be documented: python3 -c `'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Scripts for unit testing
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base.py`
