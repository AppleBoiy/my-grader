#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: octagon_area
Class: 204111/2023 Sec TA
DATE: 00:58 17/7/2023 AD
"""


def main():
    x = float(input('X: '))
    print(f'{octagon_area(x):.2f}')


def octagon_area(side_length):
    """
    Calculates and returns the area of an octagon given the side length.
    """
    full_area = side_length ** 2
    outer_white_area = ((side_length / 3) ** 2) * 2
    return full_area - outer_white_area


if __name__ == '__main__':
    main()
