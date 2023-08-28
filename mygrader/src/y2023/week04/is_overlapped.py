#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: is_overlapped
Class: 204111/2023 Sec TA
DATE: 01:00 17/7/2023 AD
"""


def main():
    test()


def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):
    """
    Check if two rectangles overlap.

    Arguments:
    l1, t1: The left and top coordinates of the first rectangle.
    w1, h1: The width and height of the first rectangle.
    l2, t2: The left and top coordinates of the second rectangle.
    w2, h2: The width and height of the second rectangle.

    Returns:
    True if the rectangles overlap, False otherwise.
    """
    if l2 > l1 + w1:
        return False
    if t2 > t1 + h1:
        return False
    if l2 + w2 < l1:
        return False
    if t2 + h2 < t1:
        return False
    return True


def test():
    print("All tests cases passed successfully.")


if __name__ == '__main__':
    main()
