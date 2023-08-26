#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: decodeV3.1 (short_comment)
Class: 204111/2023 Sec TA
DATE: 01:20 1/8/2023 AD
"""


# Decode a character from the code_table using the str_index.
def decode_helper(code_table: str, str_index: str) -> str:
    # Special case: Return a newline character when the str_index is a period ('.').
    if str_index == ".":
        return "\n"

    table_length = len(code_table)
    idx = int(str_index)

    if -table_length <= idx < table_length:
        return code_table[idx]
    # If the index is out of bounds, return an underscore symbol as a fallback.
    return '_'


# Decode the input text using the provided code_table.
def decode(code_table: str, text: str) -> str:
    decoded_words = map(lambda x: decode_helper(code_table, x), text.split())
    decoded_text = ''.join(decoded_words)
    return decoded_text
