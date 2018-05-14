#!/usr/bin/env python
"""
The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:
    F1  = 1
    F2  = 1
    F3  = 2
    F4  = 3
    F5  = 5
    F6  = 8
    F7  = 13
    F8  = 21
    F9  = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.
    >>> main(3)
    12

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
    >>> main(1000)
    4782
"""
from __future__ import division


def main(digits):
    """
        Find the index of the first term in the Fibonacci sequence to contain the
    given number of digits.

    :param digits: Number of digits that the requested term should contains.
    :rtype: int
    """
    # The number of digits of the Fibonacci terms is increased according to the
    # following sequences, where the values in the list are the number of terms
    # with the specified number of digits (=index), starting from 1-digit -> 1th term.
    initial = [0, 6, 5, 5]
    # .................................after the first 4-digit term, the pattern
    # below is repeated continuously
    pattern = [4, 5, 5, 5, 4, 5, 5, 5, 5, 4, 5, 5, 5, 5]
    length = 14  # ....................instead of: len(pattern)

    if digits < 5:
        return sum(initial[:digits]) + 1

    digits -= 4
    index = ((digits // length) * sum(pattern)) + sum(pattern[:(digits % length)])
    return index + 16  # ..............instead of: sum(initial)