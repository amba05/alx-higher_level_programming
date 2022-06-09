#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ans = {}
    for i in sorted(a_dictionary.keys()):
        ans[i] = a_dictionary[i] * 2
    return ans


