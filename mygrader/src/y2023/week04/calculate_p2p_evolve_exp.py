#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: calculate_p2p_evolve_exp
Class: 204111/2023 Sec TA
DATE: 00:59 17/7/2023 AD
"""


def main():
    test()


def calculate_p2p_evolve_exp(pidgey, candy):
    """
    Calculates the evolution experience points from evolution Pidgey to Pidgeotto.

    Args:
        pidgey (int): The number of Pidgey.
        candy (int): The number of candies available.

    Returns:
        int: The evolution experience points from evolution Pidgey to Pidgeotto.
    """
    evolution_count = (pidgey + candy - 2) // 11
    if pidgey == 0:
        return 0
    return min(evolution_count, pidgey) * 500


def test():
    assert calculate_p2p_evolve_exp(1, 12) == 500
    assert calculate_p2p_evolve_exp(0, 19) == 0
    assert calculate_p2p_evolve_exp(2, 12) == 500
    assert calculate_p2p_evolve_exp(2, 22) == 1000

    print("All tests cases passed successfully.")


if __name__ == '__main__':
    main()
