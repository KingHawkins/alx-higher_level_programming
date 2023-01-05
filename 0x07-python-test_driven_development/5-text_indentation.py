#!/usr/bin/python3
def text_indentation(text):
    """Implementing

    Args:
        string(str): text to be printed

    Raises:
        TypeError: text must be a string

    """
    if isinstance(text, (int, list)) or isinstance(text, (float, tuple)):
        raise TypeError("text must be a string")
    if isinstance(text, str):
        if (text[len(text)-1] == '.' or text[len(text)-1] == '?'
                or text[len(text)-1] == ',') or text[len(text)-1]==':':
            print("\n\n")
    arr = ['?', '.', ':']
    array = list(text)
    for item in range(len(array)):
        if array[item] in arr:
            array[item + 1] = '\n\n'
    print(''.join(array))

