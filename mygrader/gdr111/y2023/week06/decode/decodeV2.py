#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: decodeV2
Class: 204111/2023 Sec TA
DATE: 01:43 24/7/2023 AD
"""


def decode(code_table, text):
    result = ""
    for line in text.splitlines():
        if line == '.' or line[-1] != '.':
            continue
        list_index = line.split()
        for item in list_index[:-1]:
            index = int(item)

            if index < 0 or index >= len(code_table):
                result += '_'
            else:
                result += code_table[index]
        result += '\n'

    return result
