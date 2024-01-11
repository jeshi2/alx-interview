#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    - data: A list of integers representing 1 byte of data each.

    Returns:
    - True if data is a valid UTF-8 encoding, else return False.
    """
    # keep track of of remaining bytes for the current character
    remaining_bytes = 0

    for byte in data:
        mask = 1 << 7
        if not remaining_bytes:
            while byte & mask:
                remaining_bytes += 1
                mask >>= 1
            if not remaining_bytes:
                continue
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        remaining_bytes -= 1
    return remaining_bytes == 0
