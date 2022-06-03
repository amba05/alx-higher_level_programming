#!/usr/bin/python3
import sys

num = len(sys.argv)

if num == 1:
    print("{} arguments.".format(num - 1))
else:
    print("{} arguments:\n".format(num - 1))

    i = 1
    for elem in sys.argv:
        if elem != sys.argv[0]:
            print("{}: {}\n".format(i, elem))
            i+=1
