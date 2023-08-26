#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: base_b_v1
Class: 204111/2023 Sec TA
DATE: 21:35 7/8/2023 AD
"""


def base_b(number: int, base: int) -> str:
    """
    Convert a number in base ten to the given base b using recursion.

    Args:
        number (int): The number to convert (in base ten).
        base (int): The base to convert the number to (between 2 and 10).

    Returns:
        str: The converted number as a string in the given base.
    """

    if not 2 <= base <= 10:
        raise ValueError("Base must be between 2 and 10.")

    # Base case: the number is less than the base return number in the given base
    if number < base:
        return number

    quotient = number // base
    remainder = number % base

    # Recursive call to convert the quotient and append the remainder
    converted_number = base_b(quotient, base) * 10 + remainder

    return converted_number
