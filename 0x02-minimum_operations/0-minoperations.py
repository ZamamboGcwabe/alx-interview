#!/usr/bin/python3
""" write a method that calculates the fewest number of operations.
"""


def minOperations(n):
    """ calculates the fewest number of operations needed to
    result in exactly n H.
    """
    # all outputs should be at least 2 char
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 8:
            ops += root
            n = n / root
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return ops
