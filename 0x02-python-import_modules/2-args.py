#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if sys.argv[1:]:
        if sys.argv[2:]:
            print("{} arguments:".format(len(sys.argv[1:])))
        else:
            print("{} argument:".format(len(sys.argv[0:1])))
        for i in range(1, len(sys.argv[1:]) + 1):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments.".format(len(sys.argv[1:])))
