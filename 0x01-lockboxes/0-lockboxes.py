#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Initialize a set to keep track of opened boxes
    """
    opened_boxes = {0}

    """
    Initialize a list to keep track of new keys found
    """
    new_keys = list(boxes[0])

    """ Continue as long as there are new keys to explore
    """
    while new_keys:
        """Get a key from the list"""
        key = new_keys.pop()

        """
        If the key opens a new box, add it to the set of opened boxes
        """
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            new_keys.extend(boxes[key])

    """Check if all boxes can be opened"""
    return len(opened_boxes) == len(boxes)
