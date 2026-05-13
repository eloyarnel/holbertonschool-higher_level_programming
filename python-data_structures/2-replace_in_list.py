#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Check if idx is negative
    if idx < 0:
        return my_list
    # Check if idx is out of range (greater than or equal to the length of the list)
    if idx >= len(my_list):
        return my_list
    # If idx is valid, replace the element at that index
    my_list[idx] = element
    # Return the modified list
    return my_list
