#!/usr/bin/env python3
"""
Author: iccie (Chaipat Jainan)
Student ID: 650510606
Work: permutation_arrival_sequences
Class: 204111/2023 Sec TA
DATE: 17:14 25/8/2023 AD
"""

from itertools import permutations


def arrival_sequences(group1, group2):
    sequences = []
    for perm in permutations(group1 + group2):
        _sequence = '>'.join(perm)
        sequences.append(_sequence)
    return list(filter(lambda seq: prior(seq, group1, group2), sequences))


def prior(seq, queue1, queue2) -> bool:
    _seq = seq.split('>')

    queue_bus1 = filter(lambda bus: bus in queue1, _seq)
    queue_bus2 = filter(lambda bus: bus in queue2, _seq)

    return tuple(queue_bus1) == queue1 and tuple(queue_bus2) == queue2


if __name__ == '__main__':
    # Test
    result = arrival_sequences(('R2', 'R4'), ('O34', 'O22'))
    for sequence in result:
        print(sequence)
