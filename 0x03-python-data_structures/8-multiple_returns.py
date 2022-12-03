#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        new_tup = ((len(sentence), None))
    else:
        new_tup = (len(sentence), sentence[0])
        return new_tup
