#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: zodiac_element
Class: 204111/2023 Sec TA
DATE: 01:01 17/7/2023 AD
"""


# Returns the zodiac element, animal, and yin/yang for the given year.
def zodiac_element(year: int) -> str:
    return f'{yin_yang(year)} {element_year(year)} {animal_year(year)}'


# Determines the yin/yang (opposite forces) for the given year.
def yin_yang(year: int) -> str:
    if year % 2 == 0:
        return 'Yang'
    return 'Yin'


# Determines the animal of the Chinese zodiac for the given year.
def animal_year(year: int) -> str:
    animals = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat']
    animal_index = year % 12
    return animals[animal_index]


# Determines the zodiac element for the given year.
def element_year(year: int) -> str:
    elements = ['Metal', 'Water', 'Wood', 'Fire', 'Earth']
    element_index = year % 10
    return elements[element_index // 2]
