#!/usr/bin/python3
def uppercase(str):
    for elem in str:
        if ord(elem) < 97:
            print(elem, end="")

        else:
            print(chr(ord(elem) - 32), end="")
    print("\n")
