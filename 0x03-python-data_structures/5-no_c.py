#!/usr/bin/python3


def no_c(my_string):
    arr = list(my_string)
    var = []
    for i in arr:
        j = 0
        if ord(i) == ord('c') or ord(i) == ord('C'):
            j += 1
        else:
            var.append(i)

    return "".join(var)
