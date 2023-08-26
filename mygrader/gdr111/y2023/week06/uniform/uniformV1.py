#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: uniformV1
Class: 204111/2023 Sec TA
DATE: 22:07 23/7/2023 AD
"""

import string


def find_lower(word):
    # count lowercase in word
    lowercase_chars = filter(lambda char: char in string.ascii_lowercase, word)
    return len(list(lowercase_chars))


def find_upper(word):
    # count uppercase in word
    uppercase_chars = filter(lambda char: char in string.ascii_uppercase, word)
    return len(list(uppercase_chars))


def uniform(line):
    first_char_is_upper = line and line[0] in string.ascii_uppercase
    lowercase_count = find_lower(line)
    uppercase_count = find_upper(line)

    if uppercase_count > lowercase_count:
        return line.upper()
    elif lowercase_count > uppercase_count:
        return line.lower()
    else:
        return line.upper() if first_char_is_upper else line.lower()
