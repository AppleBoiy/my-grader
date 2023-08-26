#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: print_polynomial
Class: 204111/2023 Sec TA
DATE: 23:57 30/7/2023 AD
"""

from typing import List, Tuple


def print_polynomial(pc_list: List, v: str) -> str:
    # Sort the terms in descending order of exponents
    sorted_terms = sorted(pc_list, reverse=True)

    # Filter non-zero terms using the filter() function
    non_zero_terms = [*filter(lambda term: term[1] != 0, sorted_terms)]

    # If all terms have coefficient 0, the polynomial is 0
    if not non_zero_terms:
        return '0'

    # Convert each non-zero term to a string representation using map
    list_polynomial = map(lambda term: term_to_str(term, v), non_zero_terms)

    # Combine all terms into the polynomial string using join
    polynomial_raw = ' '.join(list_polynomial)

    # Remove redundant spaces and adjust the formatting
    remove_space = polynomial_raw.replace(f' 1{v}', ' ' + v).lstrip('+')

    # Adjust the negative sign if present
    return remove_space.strip() if remove_space[0] != '-' else '-' + remove_space[2:]


# Convert a polynomial term to its string representation.
def term_to_str(term: Tuple[int, int], v: str) -> str:
    exponent, coefficient = term

    # Determine the sign of the coefficient and convert it to positive if necessary
    sign = '-' if coefficient < 0 else '+'
    coefficient = abs(coefficient)

    if exponent == 0:
        # Case 1: Constant term (variable^0)
        return f"{sign} {coefficient}"
    elif abs(exponent) == 1:
        # Case 2: Exponent is 1
        return f"{sign} {coefficient}{v}"
    else:
        # Case 3: Normal term with both coefficient and exponent
        return f"{sign} {coefficient}{v}^{exponent}"
