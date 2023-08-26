#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: medal_allocation
Class: 204111/2023 Sec TA
DATE: 15:00 31/7/2023 AD
"""
from typing import List, Sequence


def find_medal(lst: List) -> Sequence:
    # Sort the list and remove zeros
    lst = sorted(filter(lambda x: x != 0, lst))

    # If the list is empty after removing zeros.
    if not lst:
        return [], [], []

    # Find the gold medalists (greater than or equal to the maximum number)
    g_idx = lst.index(max(lst))
    gold, s_lst = lst[g_idx:], lst[:g_idx]

    # If there are no numbers less than the maximum (silver medalists),
    # then all numbers in the list are equal, so only gold medalists are awarded
    if not s_lst:
        return gold, [], []

    # Find the silver medalists (greater than or equal to the maximum number in the remaining list)
    s_idx = s_lst.index(max(s_lst))
    silver, b_lst = s_lst[s_idx:], s_lst[:s_idx]

    # If there are no numbers less than the maximum (bronze medalists),
    # then only gold and silver medalists are awarded
    if not b_lst:
        return gold, silver, []

    # Find the bronze medalists (greater than or equal to the maximum number in the remaining list)
    bronze = b_lst[b_lst.index(max(b_lst)):]
    return gold, silver, bronze


def medal_allocation(lst: List[int]) -> Sequence:
    # Find the medalists from the given list
    gold, silver, bronze = find_medal(lst)

    # If there are no gold medalists, return empty lists for all medals
    if not gold:
        return [], [], []

    if len(gold) == 1:
        # Only one gold medalist
        if len(silver) >= 2:
            # More than one silver medalist, no bronze medalist
            return gold, silver, []
        # Only one silver medalist, return gold, silver, and bronze medalists
        return gold, silver, bronze
    elif len(gold) == 2:
        # Two gold medalists, no silver medalist
        return gold, [], silver
    else:
        # Three or more gold medalists, no silver or bronze medalist
        return gold, [], []
