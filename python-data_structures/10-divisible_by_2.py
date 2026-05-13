#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Returns a list of True or False values depending on
    whether each integer in the list is divisible by 2
    """

    # Create an empty list to store the results
    result = []

    # Loop through each number in the original list
    for num in my_list:
        # Check if the number is divisible by 2
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    # Return the new list with True/False values
    return result
