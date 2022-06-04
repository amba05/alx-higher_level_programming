#!/usr/bin/python3
def max_integer(my_list=[]):

    if not my_list:
        return None
    else:
        ans = sorted(my_list)
        return ans[-1]
