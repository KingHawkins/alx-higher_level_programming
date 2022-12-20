#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    val = []
    try:
        for i in range(list_length):
            val.append(my_list_1[i]/my_list_2[i])
    except Exception:
        print("division by 0")
        print("wrong type")
        try:
            for i in range(list_length):
                if my_list_2[i] == 0 or type(my_list_2[i]) == str:
                    result.append(0)
                else:
                    result.append(my_list_1[i]/my_list_2[i])
        except IndexError:
            print("out of range")
    finally:
        return (result) or val
