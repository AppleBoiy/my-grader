#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: square_frame
Class: 204111/2023 Sec TA
DATE: 14:44 28/7/2023 AD
"""
from typing import Tuple, List, Iterable


# pad numbers with leading zeros to a specified length
def pad_with_zeros(nums: List, length: int) -> List:
    return [*map(lambda num: str(num).zfill(length), nums)]


# generate a frame pattern of numbers for a given value of n
def generate_frame_pattern(n: int) -> Tuple:
    # Calculate the maximum length of the numbers after multiplication with 4 and subtracting 4
    max_length = len(str(4 * n - 4))

    # Define the four sides of the frame pattern as ranges
    frames = (
        range(1, n + 1),  # top_frame
        range(n + 1, 2 * n - 1),  # right_frame
        range(3 * n - 2, 2 * n - 2, -1),  # bottom_frame
        range(4 * n - 4, 3 * n - 2, -1),  # left_frame
    )

    # Pad the numbers in each frame with leading zeros using the pad_with_zeros function
    padded_frames = map(pad_with_zeros, frames, [max_length] * 4)
    return tuple(padded_frames)


# Returns a function to join two elements from Iterable with a specified separator and size.
def join_middle_layer(sep: str, size: int) -> callable:
    def helper(obj: Iterable) -> str:
        obj_1, obj_2 = [*obj][:2]
        separator = sep * (size - (len(obj_1) + len(obj_2)))
        return obj_1 + separator + obj_2

    return helper


# Creates the middle layer of a square frame pattern using left and right frames.
def create_middle_layer(left_frame: Iterable, right_frame: Iterable, sep: str, size: int) -> str:
    # Pair corresponding elements from left_frame and right_frame.
    side_frame = zip(left_frame, right_frame)

    # Join each pair with the separator and size.
    middle_layer = map(join_middle_layer(sep, size), side_frame)

    # Join the resulting lines into a single string with newlines as separators.
    return "\n".join(middle_layer)


# Generates and prints a square frame pattern with a given size n.
def square_frame(n: int, sep: str = " ") -> None:
    # Get the top, right, bottom, and left frames of the square frame.
    top, right, bottom, left = generate_frame_pattern(n)

    # Join the frames using the specified separator sep to create the top and bottom corners.
    top_corner = sep.join(top)
    bot_corner = sep.join(bottom)

    # Calculate the size of the square and create the middle layer using the create_middle_layer function.
    size_square = len(top_corner)
    mid_corner = create_middle_layer(left, right, sep, size_square)

    # Assemble the square by joining the top corner, middle layer,
    # and bottom corner with newline characters as separators.
    square = "\n".join((top_corner, mid_corner, bot_corner))

    # Print the square frame pattern.
    print(square)


if __name__ == '__main__':
    for i in range(3, 25):
        square_frame(i, "_")
        print()
