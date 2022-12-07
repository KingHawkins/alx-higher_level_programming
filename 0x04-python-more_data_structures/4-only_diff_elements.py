#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    for item in set_1:
       if item not in set_2:
          new.append(item)
    for item in set_2:
       if item not in set_1:
          new.append(item)
    return new
