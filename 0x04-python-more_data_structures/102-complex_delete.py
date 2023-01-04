#!/usr/bin/python3
def let_filter(a_dic):
    new = []
    for item in a_dic:
        if item not in new:
            new.append(item)
            return True
    else:
        return False


def complex_delete(a_dictionary, value):
    new = dict()
    new_lis = list(a_dictionary.values())
    if a_dictionary:
        if value in a_dictionary.values():
            new = {key: a_dictionary[key] for key in a_dictionary if key not in new_lis}
        else:
            return new
    else:
        return a_dictonary
