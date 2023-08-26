#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: base_b_v2
Class: 204111/2023 Sec TA
DATE: 21:56 19/8/2023 AD
"""


def base_b(number: int, b: int) -> str:
    if number < b:
        return number

    return base_b(number // b, b) * 10 + number % b
