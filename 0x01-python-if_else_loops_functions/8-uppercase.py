#!/usr/bin/python3
def uppercase(strin):
    copied = strin[:]
    dic = {'a': 65, 'b': 66, 'c': 67, 'd': 68, 'e': 69, 'f': 70, 'g': 71, 'h': 72, 'i': 73, 'j': 74, 'k': 75, 'l': 76, 'm': 77, 'n': 78, 'o': 79, 'p': 80, 'q': 81, 'r': 82, 's': 83, 't': 84, 'u': 85, 'v': 86, 'w': 87, 'x': 88, 'y': 89, 'z': 90}

    select = ''
    new = ''
    for key in dic.keys():
        if key in copied:
            select = select + chr(dic[key])
        elif key not in copied:
            new = new + copied.replace(key, "")

    final = str(new) + select
    print("{}".format(final))


uppercase("Best School")
