#!/usr/bin/env python3
"""
Author: Chaipat Jainan
Student ID: 650510606
Work: decode
Class: 204111/2023 Sec TA
DATE: 22:31 23/7/2023 AD
"""


def decode(code_table: str, text: str) -> str:
    # Decode the text using the provided code table.

    # Split the input text into lines
    lines = text.splitlines()

    # Decode each line by applying the decode_line function to it
    decoded_lines = map(decode_line(code_table), lines)

    # Join the decoded lines to form the final decoded text
    decoded_text = '\n'.join(decoded_lines)
    return decoded_text


def decode_line(code_table: str) -> callable:
    # Create a function to decode a single line of text using the provided code table.
    def helper(line: str) -> str:
        # Split the line into individual elements and decode each element using the decode_helper function
        elements = line[:-1].split()  # Assuming there is a dot('.') at the end of line.
        decoded_elements = map(decode_helper(code_table), elements)
        return ''.join(decoded_elements)

    return helper


# Create a function to decode an element using the code table.
def decode_helper(code_table: str) -> callable:
    def helper(str_index) -> str:
        # Convert the string index to an integer and check if it is within the valid range of the code table
        idx = int(str_index)
        if -len(code_table) <= idx < len(code_table):
            return code_table[idx]
        return '_'

    return helper
