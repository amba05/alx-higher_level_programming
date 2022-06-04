#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    val_1 = len(tuple_a)
    val_2 = len(tuple_b)
    tup = ()

    if val_2 == 0:
        tup = tup + ((tuple_a[0] + 0), )
        tup = tup + ((tuple_a[1] + 0), )
    
    elif val_2 < 2:
        tup = tup + ((tuple_a[0] + tuple_b[0]), )
        tup = tup + ((tuple_a[1] + 0), )
    
    else:
        tup = tup + ((tuple_a[0] + tuple_b[0]), )
        tup = tup + ((tuple_a[1] + tuple_b[1]), )

    return tup
