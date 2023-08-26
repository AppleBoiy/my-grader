#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: median_of_median
Class: 204111/2023 Sec TA
DATE: 15:10 25/8/2023 AD
"""

from typing import List, Union


def my_id() -> str:
    return '650510606'


def median_of_median(list_a: List[Union[int, float]]) -> Union[int, float]:
    # Base cases
    if len(list_a) == 1:
        return list_a[0]

    if len(list_a) == 2:
        return sum(list_a) / 2

    # Calculate sublist size
    sub_size = len(list_a) // 3

    # Divide the list into sublist
    sub1 = list_a[:sub_size]
    sub2 = list_a[sub_size:2 * sub_size]
    sub3 = list_a[2 * sub_size:]

    # Recursively find medians of sublist
    med1 = median_of_median(sub1)
    med2 = median_of_median(sub2)
    med3 = median_of_median(sub3)

    # Calculate median of medians
    med_of_meds_lst = [med1, med2, med3]

    # Calculate final median
    return sorted(med_of_meds_lst)[1]
