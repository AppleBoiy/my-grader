#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: sort_is_anagram
Class: 204111/2023 Sec TA
DATE: 13:56 10/8/2023 AD
"""


def is_anagram(s1: str, s2: str) -> bool:
    # Clean the input strings by removing non-alphabetic characters and converting to lowercase
    s1_cleaned = filter(str.isalpha, s1.lower())
    s2_cleaned = filter(str.isalpha, s2.lower())

    return sorted(s1_cleaned) == sorted(s2_cleaned)
