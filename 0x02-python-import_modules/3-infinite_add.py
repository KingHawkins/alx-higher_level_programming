#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    if sys.argv[1:]:
        for i in range(1, len(sys.argv[1:]) + 1):
            sum = sum + int(sys.argv[i])

    print("{}".format(sum))
