#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: reverse_digits_v2
Class: 204111/2023 Sec TA
DATE: 02:05 7/8/2023 AD
"""


def reverse_digits(number: int) -> int:
    # Handle negative numbers by recursively processing the positive counterpart
    if number < 0:
        return -reverse_digits(-number)

    # Base case: Single-digit numbers are their own reverse
    if number < 10:
        return number

    # Extract the last digit (header) and the remaining digits (trailer)
    header = number % 10
    trailer = number // 10

    # Recursively reverse the trailer
    reversed_trailer = reverse_digits(trailer)

    # Calculate the reversed number by combining the header and reversed trailer
    reversed_number = header * 10 ** len(str(trailer)) + reversed_trailer

    return reversed_number
