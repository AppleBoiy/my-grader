#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: triangleV3
Class: 204111/2023 Sec TA
DATE: 21:14 23/7/2023 AD
"""


# Generate a triangular pattern using asterisks (*) and periods (.) with the given number of rows.
def triangle(num_rows: int) -> str:
    return '\n'.join(
        map(
            lambda row: '* ' * (row + 1)
            # For the first and last row, produce a complete row of asterisks (*).
            if row in (0, num_rows - 1)
            # For inner rows, create a triangular pattern with asterisks (*) and periods (.).
            else '*' + '.' * (2 * row - 1) + '*',
            range(num_rows)
        )
    ) + '\n'
