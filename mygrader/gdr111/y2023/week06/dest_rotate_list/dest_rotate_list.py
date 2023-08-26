#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: dest_rotate_list
Class: 204111/2023 Sec TA
DATE: 21:35 23/7/2023 AD
"""
from numbers import Number
from typing import List


def dest_rotate_list(list_a: List[Number], n: int) -> None:
    """
    Rotate a list to the right by the given number of positions.

    Args:
        list_a (list[Number]): The input list to be rotated.
        n (int): The number of positions to rotate the list to the right.
    """

    # Calculate the effective number of rotation steps
    rotation_steps = n % len(list_a)

    # Create the rotated list by slicing and concatenating the parts
    rotated_list = list_a[-rotation_steps:] + list_a[:-rotation_steps]

    # Update the input list with the rotated list
    list_a.clear()
    list_a.extend(rotated_list)
