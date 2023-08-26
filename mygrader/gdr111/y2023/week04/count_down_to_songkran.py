#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: count_down_to_songkran
Class: 204111/2023 Sec TA
DATE: 00:59 17/7/2023 AD
"""


def main():
    test()


def is_leap_year(year: int) -> bool:
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


def count_down_to_songkran(day: int, month: int, year: int) -> int:
    day_left = 0

    # Calculate days left based on the month
    if month == 1:
        day_left += 103 + is_leap_year(year)  # 103 days until Songkran from 1si January
    elif month == 2:
        day_left += 72 + is_leap_year(year)  # 72 days until Songkran from 1st February
    elif month == 3:
        day_left += 44  # 44 days until Songkran from 1st March
    elif month == 4:
        day_left += 13 if day <= 13 else 365 + is_leap_year(year + 1) + 13  # Account for day of April
    elif 11 >= month >= 5:
        day_left += 348 + is_leap_year(year + 1)  # Remaining months until December
        if month >= 5:
            day_left -= 31  # Subtract days in June
        if month >= 7:
            day_left -= 30  # Subtract days in July
        if month >= 8:
            day_left -= 31  # Subtract days in August
        if month >= 9:
            day_left -= 31  # Subtract days in September
        if month >= 10:
            day_left -= 30  # Subtract days in October
        if month >= 11:
            day_left -= 31  # Subtract days in November
    else:
        day_left += 134 + is_leap_year(year + 1)  # Months after December until Songkran next year

    return day_left - day  # Calculate remaining days until Songkran


def test():
    assert count_down_to_songkran(1, 2, 2016) == 72
    assert count_down_to_songkran(13, 4, 2016) == 0

    print("All test cases passed successfully.")


if __name__ == '__main__':
    main()
