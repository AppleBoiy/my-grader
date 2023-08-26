#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: num_to_word
Class: 204111/2023 Sec TA
DATE: 16:12 31/7/2023 AD
"""
from typing import Tuple


def num_to_word(number: int) -> str:
    if number == 0:
        return 'zero'

    # Convert the given number into words based on its magnitude
    result = ""

    # Convert each part to words and concatenate them
    part1, part2, part3, part4 = split_into_parts(number)
    if part1 > 0:
        result += three_digits_to_word(part1) + ' billion '
    if part2 > 0:
        result += three_digits_to_word(part2) + ' million '
    if part3 > 0:
        result += three_digits_to_word(part3) + ' thousand '
    if part4 > 0:
        result += three_digits_to_word(part4)
    return result.strip()


def split_into_parts(number: int) -> Tuple[int, int, int, int]:
    # Ensure the input is valid (positive 12-digit integer)
    if not isinstance(number, int) or number < 0 or number > 999_999_999_999:
        raise ValueError("Input must be a positive 12-digit integer.")

    # Ensure the number has 12 digits by adding leading zeros if necessary
    num_str = str(number).zfill(12)

    # Split the 12-digit number into chunks of 3 digits each
    part1 = int(num_str[:3])
    part2 = int(num_str[3:6])
    part3 = int(num_str[6:9])
    part4 = int(num_str[9:])

    return part1, part2, part3, part4


def three_digits_to_word(number: int) -> str:
    # Define lists of words for units, tens, and hundreds
    units_words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens_words = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                   "nineteen"]
    tens_words = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # Separate the digits of the number
    hundreds = number // 100
    tens = (number // 10) % 10
    units = number % 10

    # Convert the number to words
    result = ""
    if hundreds > 0:
        result += units_words[hundreds] + " hundred"

    if tens == 1:
        # Numbers 10 to 19 are treated as special cases
        result += " " + teens_words[units]
    else:
        if tens > 0:
            result += " " + tens_words[tens]
        if units > 0:
            result += "-" if tens > 0 else " "
            result += units_words[units]

    return result.strip()  # Remove leading/trailing spaces
