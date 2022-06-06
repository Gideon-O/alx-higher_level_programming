#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_num = len(sys.argv)
    if arg_num == 1:
        print("0 argument.")
    else:
        print("{:d} arguments: ".format(arg_num))
        for arg in range(0, arg_num):
            print("{:d}: {:s}".format(arg, sys.argv[arg]))
