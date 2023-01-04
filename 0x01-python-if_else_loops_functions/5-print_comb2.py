#!/usr/bin/python3
res = ''
for i in range(0, 100):
    if i < 10:
        res = res + str(0) + str(i) + ',' + ' '
    elif i != 99:
        res = res + str(i) + ',' + ' '
    else:
        res = res + str(i)


print("{}".format(res))
