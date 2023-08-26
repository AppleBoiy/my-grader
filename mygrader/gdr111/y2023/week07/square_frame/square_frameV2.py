#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: square_frameV2
Class: 204111/2023 Sec TA
DATE: 16:41 30/7/2023 AD
"""

from typing import Iterable, List, Tuple


def generate_frame_pattern(n: int) -> Tuple:
    def pad_with_zeros(nums: List, length: int) -> List:
        return [*map(lambda num: str(num).zfill(length), nums)]

    max_length = len(str(4 * n - 4))
    frames = (
        range(1, n + 1),
        range(n + 1, 2 * n - 1),
        range(3 * n - 2, 2 * n - 2, -1),
        range(4 * n - 4, 3 * n - 2, -1)
    )

    return tuple(map(lambda nums: pad_with_zeros(nums, max_length), frames))


def create_middle_layer(left_frame: Iterable, right_frame: Iterable, sep: str, size: int) -> str:
    return "\n".join(
        map(
            lambda lr: str(lr[0]) + sep * (size - len(str(lr[0]) + str(lr[1]))) + str(lr[1]),
            zip(left_frame, right_frame)
        )
    )


def square_frame(n: int, sep: str = " ") -> None:
    top, right, bottom, left = generate_frame_pattern(n)
    top_corner = sep.join(top)
    bot_corner = sep.join(bottom)
    mid_corner = create_middle_layer(left, right, sep, len(top_corner))
    print("\n".join((top_corner, mid_corner, bot_corner)))


if __name__ == '__main__':
    for i in range(3, 25):
        square_frame(i, "_")
        print()
