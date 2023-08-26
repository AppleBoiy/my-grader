#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: pi_v2
Class: 204111/2023 Sec TA
DATE: 22:00 19/8/2023 AD
"""


def pi(n):
    if n == 0:
        return 3

    Pi_n = 4 / (2 * n * (2 * n + 1) * (2 * n + 2))

    if n % 2 == 0:
        Pi_n = -Pi_n

    return pi(n - 1) + Pi_n
