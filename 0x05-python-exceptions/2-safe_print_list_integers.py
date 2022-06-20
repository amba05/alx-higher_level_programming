#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for j in my_list:
        a += 1

    i = 0
    num = 0
    while i < x:
        val = type(my_list[i])
        if val == int:
            try:
                print("{:d}".format(my_list[i]), end="")
                num += 1
            except str:
                pass
        i += 1
    print()
    return num

