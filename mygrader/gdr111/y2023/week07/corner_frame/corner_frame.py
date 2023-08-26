#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: corner_frame
Class: 204111/2023 Sec TA
DATE: 12:53 27/7/2023 AD
"""
from typing import Iterable


def corner_frame(n: int) -> str:
    nums = range(1, n + 1)

    # Map each line of the corner frame using the increase_left function
    lines = map(lambda x: increase_left(nums, x), nums)

    # Convert each line to a space-separated string
    lines = map(lambda line: " ".join(line), lines)

    # Join the lines with a newline character and return the result
    return "\n".join(lines) + "\n"


def increase_left(_iter: Iterable, _max: int) -> Iterable:
    return map(lambda item: str(item) if item >= _max else str(_max), _iter)
