#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        new_tup = ((len(sentence), None))
    else:
        length = len(sentence)
        first_char = sentence[0]
        new_tup = (length, first_char)
        return new_tup
