#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
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
        # Check if the most significant bit is set
        if remaining_bytes == 0:
            if (byte >> 7) == 0b0:
                continue
            elif (byte >> 5) == 0b110:
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3
            else:
                return False
        else:
            # Check if the two most significant bits are 0b10
            if (byte >> 6) != 0b10:
                return False

            remaining_bytes -= 1

    return remaining_bytes == 0
