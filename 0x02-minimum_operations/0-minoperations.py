#!/usr/bin/python3
""" write a method that calculates the fewest number of operations.
"""


def minOperations(n):
    """ calculates the fewest number of operations needed to
    result in exactly n H.
    """
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 8:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops
