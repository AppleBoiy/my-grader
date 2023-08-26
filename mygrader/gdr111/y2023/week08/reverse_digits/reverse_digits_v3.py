#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: reverse_digits_v3
Class: 204111/2023 Sec TA
DATE: 18:27 13/8/2023 AD
"""


def reverse_digits(number: int, reversed_number: int = 0) -> int:
    # Handle negative numbers by recursively processing the positive counterpart
    if number < 0:
        return -reverse_digits(-number)

    # Base case: If the input number is 0, the reversed number is complete
    if number == 0:
        return reversed_number

    return reverse_digits(number // 10, reversed_number * 10 + number % 10)
