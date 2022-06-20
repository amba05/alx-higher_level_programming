#!/usr/bin/python3
def safe_print_integer(value):
    val = isinstance(value, int)
    if val:
        try:
            print("{:d}".format(value))
            return True
        except:
            return False
