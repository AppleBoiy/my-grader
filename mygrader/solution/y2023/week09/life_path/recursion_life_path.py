#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: recursion_life_path
Class: 204111/2023 Sec TA
DATE: 18:44 25/8/2023 AD
"""


def my_id() -> str:
    return '650510606'


def life_path(n: int) -> int:
    if n < 10:
        return n

    return life_path(sum(map(int, str(n))))
