#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: dest_arrival_sequences
Class: 204111/2023 Sec TA
DATE: 17:14 25/8/2023 AD
"""

from typing import List, Tuple


def my_id() -> str:
    return '650510606'


def queue_bus(result, prefix, seq1, seq2) -> None:
    if not seq2 and not seq1:
        # Joining the prefix to form a complete sequence
        result.append('>'.join(prefix))

    if seq1:
        queue_bus(result, prefix + [seq1[0]], seq1[1:], seq2)

    if seq2:
        queue_bus(result, prefix + [seq2[0]], seq1, seq2[1:])


def arrival_sequences(left_lane: Tuple[str], right_lane: Tuple[str]) -> List[str]:
    result = []
    queue_bus(result, [], left_lane, right_lane)
    return result


if __name__ == '__main__':
    # Test
    output = arrival_sequences(
        ('R2', 'R4'),
        ('O34', 'O22')
    )
    for item in output:
        print(item)
