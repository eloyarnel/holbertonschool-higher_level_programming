#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list[:]
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return new_list
    # If idx is valid, replace the element in the new list
    new_list[idx] = element
    # Return the new list
    return new_list
