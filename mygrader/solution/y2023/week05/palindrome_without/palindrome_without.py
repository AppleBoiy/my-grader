#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: palindrome_without
Class: 204111/2023 Sec TA
DATE: 01:29 17/7/2023 AD
"""


def palindrome_without(text: str, c: str) -> bool:
    text = text.lower().replace(' ', '').replace(c, '')
    return text == text[::-1] and len(text) > 0
