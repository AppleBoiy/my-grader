#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: triangleV2
Class: 204111/2023 Sec TA
DATE: 21:14 23/7/2023 AD
"""


# Generate a triangular pattern using asterisks (*) and periods (.) with the given number of rows.
def triangle(num_rows: int) -> str:
    # Helper function to create a row of asterisks and periods based on the row number.
    def create_row(row):
        if row == 0 or row == num_rows - 1:
            # For the first and last row, produce a complete row of asterisks (*).
            return '* ' * (row + 1)
        else:
            # For inner rows, create a triangular pattern with asterisks (*) and periods (.).
            num_periods = 2 * row - 1
            return '*' + '.' * num_periods + '*'

    # Use the 'map' function to apply the 'create_row' function to each element in the 'range(num_rows)' sequence.
    triangle_rows = map(create_row, range(num_rows))

    # Join all the rows with a newline character '\n' to form the triangle pattern as a single string.
    return '\n'.join(triangle_rows) + '\n'
