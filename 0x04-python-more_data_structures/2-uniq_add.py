#!/usr/bin/python3
def uniq_add(my_list=[]):
    ans = 0
    for i in set(my_list):
        ans = ans + i
    return ans
