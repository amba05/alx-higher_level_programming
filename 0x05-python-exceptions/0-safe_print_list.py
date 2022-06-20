#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for j in my_list:
        a += 1

    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")

        except IndexError:
            print()
            return a
        i += 1
    print()
    return i
