#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')

    if len(last_name) == 0 & len(first_name) > 0:
        print("My name is {}".format(first_name))

    elif len(first_name) == 0 & len(last_name) > 0:
        raise ValueError('First_name is empty')

    elif len(first_name) == 0 and len(last_name) == 0:
        raise ValueError('First_name is empty')

    else:
        print("My name is {} {}".format(first_name, last_name))
