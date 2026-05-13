#!/usr/bin/python3
def element_at(my_list, idx):
    # Check if idx is negative
    if idx < 0:
        return None
    # Check if idx is out of range (greater than or equal to the length of the list)
    if idx >= len(my_list):
        return None
    # If idx is valid, return the element at that index
    return my_list[idx]
