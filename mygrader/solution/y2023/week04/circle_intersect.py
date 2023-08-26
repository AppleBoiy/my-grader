#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: circle_intersect
Class: 204111/2023 Sec TA
DATE: 01:00 17/7/2023 AD
"""

import math


def main():
    test_circle_intersect()


def euclidean_distance(x1, y1, x2, y2):
    """
    Calculates the Euclidean distance between two points.

    Args:
        x1 (float): x-coordinate of the first point.
        y1 (float): y-coordinate of the first point.
        x2 (float): x-coordinate of the second point.
        y2 (float): y-coordinate of the second point.

    Returns:
        float: The Euclidean distance between the two points.
    """
    return math.hypot(x2 - x1, y2 - y1)


def circle_intersect(x1, y1, r1, x2, y2, r2, epsilon=1e-6):
    """
    Determines the intersection status between two circles.

    Args:
        x1 (float): x-coordinate of the center of the first circle.
        y1 (float): y-coordinate of the center of the first circle.
        r1 (float): radius of the first circle.
        x2 (float): x-coordinate of the center of the second circle.
        y2 (float): y-coordinate of the center of the second circle.
        r2 (float): radius of the second circle.
        epsilon (float, optional): Tolerance for floating-point comparisons. Defaults to 1e-6.

    Returns:
        int: Intersection status between the two circles.
             0: The circles intersect at exactly one point.
            -1: The circles do not intersect.
             1: The circles intersect at two distinct points.
    """
    distance = euclidean_distance(x1, y1, x2, y2)
    if math.isclose(distance, r1 + r2, abs_tol=epsilon):
        return 0
    return -1 if distance > r1 + r2 else 1


def test_circle_intersect():
    assert circle_intersect(2, 3, 5, 5, 7, 1) == 1
    assert circle_intersect(0, 0, 2.5, 3, 4, 2.5) == 0
    assert circle_intersect(1, 1, 5, 6, 17, 7) == -1

    # now using specified epsilon
    assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon=1.5) == 0
    print("all ok!")


if __name__ == '__main__':
    main()
