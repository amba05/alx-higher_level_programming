#!/usr/bin/python3
def text_indentation(text):
    tok = ['.', '?', ':']

    if type(text) != str:
        raise TypeError('text must be a string')

    text_len = len(text)

    j = 0

    while j < text_len:
        if text[j] in tok:
            print("{}".format(text[j]), end="")
            j += 2
            print("{}".format("\n"))
        else:
            print("{}".format(text[j]), end="")
            j += 1
