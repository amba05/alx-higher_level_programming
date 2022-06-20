#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else: 
        num = ans = den = 0
        for i in my_list:
            num = num + (i[0] * i[1])
            den = den + i[1]
        ans = num / den
        return ans

