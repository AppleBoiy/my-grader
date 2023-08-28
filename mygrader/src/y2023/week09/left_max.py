#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: left_max
Class: 204111/2023 Sec TA
DATE: 15:00 25/8/2023 AD
"""
from typing import List


def my_id() -> str:
    return '650510606'


def left_max(list_a: List[int]) -> List[int]:
    if len(list_a) == 1:
        return list_a

    return [list_a[0]] + left_max([max(list_a[:2])] + list_a[2:])


if __name__ == '__main__':
    assert left_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert left_max([2, 8, 1]) == [2, 8, 8]
    assert left_max([1]) == [1]

    print("All tests cases passed!")
