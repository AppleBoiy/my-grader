#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: patterned_message
Class: 204111/2023 Sec TA
DATE: 14:47 25/8/2023 AD
"""


def my_id() -> str:
    return '650510606'


def patterned_message(message: str, pattern: str) -> None:
    if not pattern:
        return

    message = message.replace(' ', '')

    char: str = pattern[0]
    tailer = pattern[1:]

    if char == '*':
        print(message[0], end='')
        message = message[1:] + message[0]
    else:
        print(char, end='')

    patterned_message(message, tailer)


if __name__ == '__main__':
    patterned_message("D and C", '''
    ***************
    ******   ******
    ***************
    ''')
