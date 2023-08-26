#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: map_is_anagram
Class: 204111/2023 Sec TA
DATE: 13:57 10/8/2023 AD
"""

from string import ascii_uppercase as upcase


def is_anagram(s1: str, s2: str) -> bool:
    # Clean the input strings by removing non-alphabetic characters and converting to uppercase
    s1_cleaned = [*filter(str.isalpha, s1.upper())]
    s2_cleaned = [*filter(str.isalpha, s2.upper())]

    # Check if the count of each uppercase letter is the same in both cleaned strings
    return all(map(lambda char: s1_cleaned.count(char) == s2_cleaned.count(char), upcase))
