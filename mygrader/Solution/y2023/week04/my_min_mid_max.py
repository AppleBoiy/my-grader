#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: my_min_mid_max
Class: 204111/2023 Sec TA
DATE: 01:01 17/7/2023 AD
"""


def main():
    ...


def my_min_mid_max(a, b, c):
    # Determine the minimum and maximum values
    if a >= b:
        maximum = a
        minimum = b
    else:
        maximum = b
        minimum = a

    # Determine the middle value
    middle = c

    # Update the middle, maximum, and minimum values if necessary
    if c > maximum:
        middle = maximum
        maximum = c

    if c < minimum:
        middle = minimum
        minimum = c

    # Print the minimum, middle, and maximum values
    print("min =", minimum)
    print("mid =", middle)
    print("max =", maximum)


if __name__ == '__main__':
    main()
