#!/usr/bin/python3
"""
Module to calculate the fewest number of operations to reach n
'H' characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to reach n
    'H' characters.

    Returns:
    - int: The minimum number of operations. If n is impossible
    to achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
