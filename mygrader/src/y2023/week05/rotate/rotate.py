#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: rotate
Class: 204111/2023 Sec TA
DATE: 02:11 17/7/2023 AD
"""


def rotate(num: int, pos: int) -> int:
    num_str = str(num)
    shift = pos % len(num_str)
    return int(num_str[-shift:] + num_str[:-shift])
