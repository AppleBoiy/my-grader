#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: recursion_gcd_v2
Class: 204111/2023 Sec TA
DATE: 20:24 10/8/2023 AD
"""


def gcd(x, y):
    if x % y == 0:
        return abs(y)  # gcd for integers is always a positive number

    return gcd(y, x % y)
