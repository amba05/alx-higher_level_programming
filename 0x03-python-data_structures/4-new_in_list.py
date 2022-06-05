#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Return a new list"""
    if idx >= len(my_list) or idx < 0:
        return my_list
    copy = my_list[:]
    copy[idx] = element
    return copy
