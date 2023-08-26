#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: pi_v1
Class: 204111/2023 Sec TA
DATE: 02:46 7/8/2023 AD
"""


def pi(n):
    if n == 0:
        return 3

    # Calculate the denominator of the current term in the series
    denominator = 2 * n * (2 * n + 1) * (2 * n + 2)

    # Calculate the value of the current term
    term_value = (-1) ** n * (4 / denominator)

    # Recursively calculate the prev term and subtract it from the current approximation
    return pi(n - 1) - term_value
