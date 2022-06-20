#!/usr/bin/python3
def safe_print_integer(value):
    val = type(value)
    if val == int:
        try:
            print("{:d}".format(value))
            return True
        except str:
            return false
