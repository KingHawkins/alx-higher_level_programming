#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list_hidden = dir(hidden_4)
    for i in range(0, len(list_hidden)):
        if '__' in list_hidden[i]:
            continue
        else:
            print(list_hidden[i])
