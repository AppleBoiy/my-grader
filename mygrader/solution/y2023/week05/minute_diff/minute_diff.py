#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: minute_diff
Class: 204111/2023 Sec TA
DATE: 01:01 17/7/2023 AD
"""


def minute_diff(hour1, minute1, period1, hour2, minute2, period2) -> int:
    # Convert 12-hour format to 24-hour format by setting 12 to 0
    if hour1 == 12:
        hour1 = 0
    if hour2 == 12:
        hour2 = 0

    # Calculate the total minutes for each time
    minutes1 = calculate_minutes(hour1, minute1, period1)
    minutes2 = calculate_minutes(hour2, minute2, period2)

    # Calculate the absolute difference in minutes
    return abs(minutes1 - minutes2)


def calculate_minutes(hour, minute, period) -> int:
    # Calculate the base minutes by multiplying hours by 60 and adding the minutes
    base_minutes = hour * 60 + minute

    # Adjust base minutes for PM period
    if period == 'PM':
        base_minutes += 12 * 60

    return base_minutes
