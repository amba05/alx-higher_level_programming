#!/usr/bin/python3
def safe_print_integer(value):
    val = isinstance(value, int)
    ans = isinstance(value, str)
    if val and not ans:
        try:
            print("{:d}".format(value))
            return True
        except ans == True:
            return False
