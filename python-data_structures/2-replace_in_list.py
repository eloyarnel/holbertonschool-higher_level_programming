#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Check if idx is negative
    if idx < 0:
        return my_list
    # Check if idx is out of range
    if idx >= len(my_list):
        return my_list
    # Replace the element
    my_list[idx] = element
    return my_list
