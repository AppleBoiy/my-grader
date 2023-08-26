#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan) 
Student ID: 650510606
Work: square_frameV3
Class: 204111/2023 Sec TA
DATE: 16:41 30/7/2023 AD
"""


def generate_frame_pattern(n):
    def pad_frame(frame):
        return [*map(lambda num: str(num).zfill(max_length), frame)]

    max_length = len(str(4 * n - 4))
    frames = (
        range(1, n + 1),
        range(n + 1, 2 * n - 1),
        range(3 * n - 2, 2 * n - 2, -1),
        range(4 * n - 4, 3 * n - 2, -1),
    )

    padded_frames = map(pad_frame, frames)
    return tuple(padded_frames)


def create_middle_layer(left_frame, right_frame, sep, size):
    def join_frame_elements(lr):
        left, right = lr
        return f"{left}{sep * (size - len(left) - len(right))}{right}"

    return "\n".join(
        map(join_frame_elements, zip(left_frame, right_frame))
    )


def square_frame(n, sep=" "):
    top, right, bottom, left = generate_frame_pattern(n)
    top_corner = sep.join(map(str, top))
    bot_corner = sep.join(map(str, bottom))
    mid_corner = create_middle_layer(left, right, sep, len(top_corner))
    print("\n".join((top_corner, mid_corner, bot_corner)))


if __name__ == '__main__':
    for i in range(3, 25):
        square_frame(i, "_")
        print()
