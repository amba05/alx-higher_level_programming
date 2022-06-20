#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    while i < list_length:
        try:
            ans = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            ans = 0
            print("division by 0")
        except TypeError:
            ans = 0
            print("wrong type")
        except IndexError:
            ans = 0
            print("out of range")
        finally:
            pass
        new_list.append(ans)
        i += 1
    return new_list
