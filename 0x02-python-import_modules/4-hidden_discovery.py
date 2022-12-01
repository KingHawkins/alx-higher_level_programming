#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list_hidden = dir(hidden_4)
    for i in range(0, len(list_hidden)):
        if '__' not in list_hidden[i]:
            print("{}".format(list_hidden[i]))
