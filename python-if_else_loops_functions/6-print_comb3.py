#!/usr/bin/python3
for first_digit in range(0, 10):
    for second in range(first_digit + 1, 10):
        if first_digit == 8 and second == 9:
            print("{:d}{:d}".format(first_digit, second))
        else:
            print("{:d}{:d}".format(first_digit, second), end=", ")
