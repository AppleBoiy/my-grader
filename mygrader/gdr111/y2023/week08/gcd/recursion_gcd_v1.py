#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: recursion_gcd_v1
Class: 204111/2023 Sec TA
DATE: 20:24 10/8/2023 AD
"""


def gcd(x, y):
    if y == 0:
        # The greatest common divisor (gcd) for any number and 0 is the absolute value of the non-zero number.
        return abs(x)  # gcd for integers is always a positive number

    # Use Euclidean algorithm: after taking the remainder of x divided by y, set y as the new x and the remainder as the new y.
    return gcd(y, x % y)
