#!/usr/bin/env python
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.
    >>> main(10)
    23

Find the sum of all the multiples of 3 or 5 below 1000.
    >>> main(1000)
    233168
"""
from __future__ import division


def sum_arithmetic_series(step, max_term):
    """
        Find the sum of the members of the given arithmetic progression.

    :param step    : The "common difference" between terms.
    :param max_term: The maximum value of the last term it could have.
    :rtype         : int
    """
    assert step < max_term, "step < max_term [{0} < {1}]".format(step, max_term)

    # .................................count all terms up to given value
    count = (max_term - 1) // step

    # .................................find the last term of the sequence
    last_term = count * step

    return (step + last_term) * count // 2


def main(max_term):
    """
        Find the sum of all the multiples of 3 or 5 below the given maximum value.

    :param max_term: The maximum value of the last term it could have.
    :rtype         : int
    """
    _return = 0

    if max_term > 3:
        _return = sum_arithmetic_series(3, max_term)

        if max_term > 5:
            _return += sum_arithmetic_series(5, max_term)

            if max_term > 15:
                return _return - sum_arithmetic_series(15, max_term)
    return _return