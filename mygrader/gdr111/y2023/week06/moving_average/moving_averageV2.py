#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: moving_averageV1
Class: 204111/2023 Sec TA
DATE: 14:38 24/7/2023 AD
"""
from numbers import Number
from typing import List, Iterable


# Calculates the moving averages of a list of numbers.
def moving_average(list_a: Iterable[Number], window_size: int) -> List[float]:
    return [
        *map(
            lambda start, end: sum(list_a[start:end]) / window_size,
            range(0, len(list_a) - window_size + 1),  # start_indices
            range(window_size, len(list_a) + 1)  # end_indices
        )
    ]


if __name__ == '__main__':
    lst = [1, 2, 3]
    w = 4
    print(moving_average(lst, w))
