#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    len_args = len(argv) - 1

    if len_args == 0:
        print("0 arguments.")
    elif len_args == 1:
        print("1 argument:")
    else:
        print(f"{len_args} arguments:")

    for i in range(1, len_args + 1):
        print(f"{i}: {argv[i]}")
