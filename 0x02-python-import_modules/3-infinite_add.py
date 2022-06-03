#!/usr/bin/python3
import sys

num = len(sys.argv)
ans = 0

if num < 2:
    print("{}".format(int(0)))
else:
    i = 1
    while i < num:
        ans = ans + int(sys.argv[i])
        i+=1
print("{}".format(ans))

