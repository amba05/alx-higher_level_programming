#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not a_dictionary:
        return None
    # best = max(a_dictionary, key=lambda x: a_dictionary[x])
    find_max = max(a_dictionary, key=a_dictionary.get)
    return find_max
