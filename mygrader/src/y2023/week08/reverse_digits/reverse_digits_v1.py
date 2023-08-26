#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: reverse_digits_v1
Class: 204111/2023 Sec TA
DATE: 02:05 7/8/2023 AD
"""


def reverse_digits(number: int, reversed_number: int = 0) -> int:
    # Base case: when the number becomes 0, return the reversed_number
    if number == 0:
        return reversed_number

    # Extract the last digit of the number
    last_digit = abs(number) % 10

    # Append the last digit to the reversed_number and remove it from the original number
    reversed_number = reversed_number * 10 + last_digit

    # Recursive call with the remaining number
    return reverse_digits(abs(number) // 10, reversed_number) * (-1 if number < 0 else 1)
