#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: moving_average
Class: 204111/2023 Sec TA
DATE: 14:38 24/7/2023 AD
"""
from typing import List


def moving_average(list_a: List[float], window_size: int) -> List[float]:
    # Generate the start and end indices for the moving windows.
    start_indices = range(0, len(list_a) - window_size + 1)
    end_indices = range(window_size, len(list_a) + 1)

    # Calculate the moving averages.
    moving_averages = map(
        lambda start, end: sum(list_a[start:end]) / window_size,
        start_indices,
        end_indices
    )

    # Convert the result of the map function into a list and return the list of moving averages.
    return list(moving_averages)

# Example usage:
# result = moving_average([1, 2, 3, 4, 5, 6], 3)
# Output: [2.0, 3.0, 4.0, 5.0]
