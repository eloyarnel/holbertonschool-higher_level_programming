#!/usr/bin/python3
"""
Module that defines a function to generate Pascal's triangle.
"""

def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle of n rows."""

    # Return empty list for non-positive integers
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Each new row starts and ends with 1
        # The inner values are the sum of the two values above them
        row = [1]

        # Build inner elements using the previous row
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
