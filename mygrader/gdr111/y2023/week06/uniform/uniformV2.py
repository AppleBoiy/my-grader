#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: uniformV2
Class: 204111/2023 Sec TA
DATE: 22:07 23/7/2023 AD
"""


def uniform(line: str) -> str:
    """
    Convert the input line to a uniform case, either all uppercase or all lowercase,
    based on the count of uppercase and lowercase characters in the input.

    Parameters:
        line (str): The input string to be converted.

    Returns:
        str: The converted string with a uniform case (all uppercase or all lowercase).

    Algorithm:
        1. Count the number of lowercase and uppercase characters in the input line.
        2. If the count of uppercase characters is greater than the count of lowercase characters,
           convert the line to all uppercase.
        3. If the count of lowercase characters is greater than the count of uppercase characters,
           convert the line to all lowercase.
        4. If the counts are equal, preserve the original case if the line is empty or starts with a
           non-alphabetic character; otherwise, convert the line to all uppercase.

    Note:
        The function avoids using explicit for loops and utilizes the built-in functions `sum` and `map`
        with lambda functions for efficient and concise code.

    Example:
        uniform("Hello World") => "HELLO WORLD"
        uniform("ChATboT") => "chatbot"
        uniform("123") => "123"
        uniform("") => ""
    """

    # Count the number of lowercase and uppercase characters in the line
    lowercase_count = sum(map(str.islower, line))
    uppercase_count = sum(map(str.isupper, line))

    # Preserve the original case if the line is empty or starts with a non-alphabetic character
    if uppercase_count == lowercase_count:
        return line.upper() if line and line[0].isupper() else line.lower()
    return line.upper() if uppercase_count > lowercase_count else line.lower()
