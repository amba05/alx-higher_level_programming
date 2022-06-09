#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in sorted(a_dictionary.keys()):
        if i == key:
            a_dictionary.pop(i)
    return a_dictionary
