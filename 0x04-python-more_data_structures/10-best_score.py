#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_key = ''
        new = list(a_dictionary.values())
        max_val = new[0]
        for key in a_dictionary:
            if a_dictionary[key] > max_val:
                max_val = a_dictionary[key]
                max_key = key
        return max_key
    else:
        return None
