#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list
    """

    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        # If invalid index, return the original list unchanged
        return my_list

    # Delete the element at the given index
    del my_list[idx]

    # Return the modified list
    return my_list
