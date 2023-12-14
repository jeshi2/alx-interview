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
    """Number of 'H' characters currently in the file"""
    current = 1
    """Number of 'H' characters in the clipboard"""
    clipboard = 1

    while current < n:
        if n % current == 0:
            clipboard = current
        current += clipboard
        operations += 1

    return operations
