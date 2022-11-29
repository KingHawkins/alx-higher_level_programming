#!/usr/bin/python3
res = ""
for i in range (10):
    for j in range (10):
        if i < j:
            if i != 8 or j != 9:
                res = res + str(i) + str(j) + ',' + ' '
            else:
                res = res + str(i) + str(j)



print(res)
