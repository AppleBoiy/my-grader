#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: set_kth_digit
Class: 204111/2023 Sec TA
DATE: 00:59 17/7/2023 AD
"""


def main():
    test_set_kth_digit()


def set_kth_digit(number, k, value):
    """
    Replaces the kth digit of a given number with the specified value.
    """
    coeff = 10 ** k
    kth = kth_digit(number, k) * coeff
    new_kth = value * coeff
    result = number - kth + new_kth
    return result


def kth_digit(number, k):
    """
    Returns the k-th digit of the given number.
    """
    value = abs(number) // 10 ** k
    return value % 10


def test_set_kth_digit():
    assert set_kth_digit(2343, 2, 7) == 2743
    assert set_kth_digit(51, 0, 2) == 52
    assert set_kth_digit(1, 2, 5) == 501


if __name__ == "__main__":
    main()
