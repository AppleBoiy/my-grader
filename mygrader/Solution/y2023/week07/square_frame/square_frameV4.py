# !/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: square_frameV4
Class: 204111/2023 Sec TA
DATE: 16:42 30/7/2023 AD
"""
from typing import Tuple, Iterable


def generate_frame_pattern(n, size: int) -> Tuple:
    # Generate the four sides of the frame pattern
    return (
        [*map(lambda num: f"{num:0{size}}", range(1, n + 1))],  # top corner
        [*map(lambda num: f"{num:0{size}}", range(n + 1, 2 * n - 1))],  # right corner
        [*map(lambda num: f"{num:0{size}}", range(3 * n - 2, 2 * n - 2, -1))],  # bottom corner
        [*map(lambda num: f"{num:0{size}}", range(4 * n - 4, 3 * n - 2, -1))],  # left corner
    )


def create_middle_layer(left_frame, right_frame: Iterable, sep: str, size: int) -> str:
    # Combine elements from left_frame and right_frame with appropriate padding
    return "\n".join(
        map(
            lambda lr: f"{lr[0]}{sep * (size - len(lr[0]) * 2)}{lr[1]}",
            zip(left_frame, right_frame)
        )
    )


def square_frame(n: int, sep: str = " ") -> None:
    # Obtain the four sides of the frame
    top, right, bottom, left = generate_frame_pattern(n, len(str(4 * n - 4)))

    # Print the complete frame with proper alignment
    print(
        sep.join(top),  # Top side
        create_middle_layer(left, right, sep, len(sep.join(top))),  # Middle layer
        sep.join(bottom),  # Bottom side
        sep="\n"
    )


if __name__ == '__main__':
    for i in range(3, 25):
        square_frame(i, "_")
        print()
