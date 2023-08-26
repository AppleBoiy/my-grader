#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: print_polynomialV2
Class: 204111/2023 Sec TA
DATE: 17:50 7/8/2023 AD
"""

from typing import List, Tuple


def print_polynomial(term_coefficients: List[Tuple[int, int]], variable_symbol: str) -> str:
    """
    Convert a polynomial from a list of (power, coefficient) tuples to a string representation.

    Args:
        term_coefficients (List[Tuple[int, int]]): List of (power, coefficient) tuples representing the terms of the polynomial.
        variable_symbol (str): Variable symbol used in the polynomial.

    Returns:
        str: String representation of the polynomial.
    """

    # Sort the terms in reverse order based on their powers
    sorted_terms = sorted(term_coefficients, reverse=True)

    # Filter out terms with a coefficient of 0
    non_zero_terms = list(filter(lambda term: term[1] != 0, sorted_terms))

    if not non_zero_terms:
        return '0'  # Return '0' if the polynomial is empty (all coefficients are 0)

    # Convert each term to its string representation
    term_strings = list(map(lambda term: term_to_str(term, variable_symbol), non_zero_terms))

    # Replace unnecessary signs and formatting in the first term
    term_strings[0] = term_strings[0].replace('- ', '-')  # Remove space after '-' sign
    term_strings[0] = term_strings[0].replace('+ ', '')  # Remove space after '+' sign

    # Join the terms with spaces to create the final polynomial string
    return ' '.join(term_strings)


def term_to_str(term: Tuple[int, int], variable_symbol: str) -> str:
    """
    Convert a single term from a (power, coefficient) tuple to its string representation.

    Args:
        term (Tuple[int, int]): Tuple representing a single term with (power, coefficient).
        variable_symbol (str): Variable symbol used in the polynomial.

    Returns:
        str: String representation of the term.

    Raises:
        ValueError: If the power is negative, as negative powers are not allowed in the polynomial.
    """

    power, coefficient = term

    if coefficient == 0:
        return ''  # Return an empty string for terms with a coefficient of 0

    if power < 0:
        raise ValueError("Negative powers are not allowed.")

    if coefficient < 0:
        sign = '-'  # Negative coefficient, so the sign is '-'
    else:
        sign = '+'  # Positive coefficient, so the sign is '+'

    # Create the string representation of the term with proper formatting
    term_string = f'{sign:s} {abs(coefficient):g}{variable_symbol:s}^{power}|'
    # Remove the variable and power part for constant terms
    term_string = term_string.replace(f'{variable_symbol:s}^0', '')
    # Remove '^1' from terms with power 1
    term_string = term_string.replace('^1|', '|')
    # Remove '1' before the variable part
    term_string = term_string.replace(f' 1{variable_symbol:s}', f' {variable_symbol:s}')

    # Remove the trailing '|' character from the term representation
    return term_string[:-1]
