#!/usr/bin/python3
"""a module tha selects a minimum operations."""


def minOperations(n):
    """ A function a method that calculates the
    fewest number of operations.
    """
    if n <= 1:
        return 0

    factors = []
    d = 2

    while n > 1:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1

    return sum(factors)
