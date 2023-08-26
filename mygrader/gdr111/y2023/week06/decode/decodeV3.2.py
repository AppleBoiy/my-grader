#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: decodeV3.2 (full_comment)
Class: 204111/2023 Sec TA
DATE: 01:22 1/8/2023 AD
"""


def decode_helper(code_table: str, str_index: str) -> str:
    """
    Decode a single character or special symbol from the code_table based on the given str_index.

    Args:
        code_table (list or dict): A table containing encoded characters and their corresponding indices.
        str_index (str): The index as a string to retrieve the character from the code_table.

    Returns:
        str: The decoded character or special symbol.
    """
    if str_index == ".":
        # Special case: Return a newline character when the str_index is a period ('.').
        return "\n"

    table_length = len(code_table)
    idx = int(str_index)

    if -table_length <= idx < table_length:
        # Check if the idx is within the valid range of the code_table.
        # If it is, return the corresponding value from the code_table.
        return code_table[idx]
    else:
        # If the index is out of bounds, return an underscore symbol as a fallback.
        return '_'


def decode(code_table: str, text: str) -> str:
    """
    Decode the text using the provided code_table.

    Args:
        code_table (list or dict): A table containing encoded characters and their corresponding indices.
        text (str): The text to be decoded.

    Returns:
        str: The decoded text.
    """
    # Split the input text into individual words using spaces as delimiters.
    words = text.split()

    # Apply the decode_helper function to each word to decode the text using the code_table.
    decoded_words = map(lambda x: decode_helper(code_table, x), words)

    # Join the decoded words together to form the final decoded text.
    decoded_text = ''.join(decoded_words)

    return decoded_text
