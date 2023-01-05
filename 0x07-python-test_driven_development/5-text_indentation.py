#!/usr/bin/python3
def text_indentation(text):
    """Implementing

    Args:
        string(str): text to be printed

    Raises:
        TypeError: text must be a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    arr = ['?', '.', ':']
    array = list(text)
    if array[len(array)-1] in arr:
        array.append(' ')
    for item in range(len(array)):
        if array[item] in arr:
            array[item + 1] = '\n\n'
    print(''.join(array), end='')
