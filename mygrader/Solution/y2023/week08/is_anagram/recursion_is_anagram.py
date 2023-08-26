#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: recursion_is_anagram
Class: 204111/2023 Sec TA
DATE: 13:56 10/8/2023 AD
"""


def is_anagram(s1: str, s2: str) -> bool:
    # Clean the input strings by removing non-alphabetic characters and converting to lowercase
    s1_cleaned = ''.join(filter(str.isalpha, s1.lower()))
    s2_cleaned = ''.join(filter(str.isalpha, s2.lower()))

    # Base case: If s1 is empty, s2 must also be empty for an anagram
    if not s1_cleaned:
        return not s2_cleaned

    # Find the index of the character in s2
    idx = s2_cleaned.find(s1_cleaned[0])

    # Recursively check the remaining characters
    return idx > -1 and is_anagram(s1_cleaned[1:], s2_cleaned[:idx] + s2_cleaned[idx+1:])
