#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Iterate from the last index to the first
    for i in range(len(my_list) - 1, -1, -1):
        # Use str.format() to print the integer
        print("{:d}".format(my_list[i]))
