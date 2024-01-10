#!/usr/bin/python3
"""
Determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Check if it's possible to unlock all boxes in a given set of boxes.
    - Each box is numbered sequentially from 0 to n - 1.
    - Each box may contain keys to the other boxes.
    - A key with the same number as a box opens that box.
    - We can assume all keys will be positive integers.
    - There can be keys that do not have boxes.
    - The first box boxes[0] is unlocked.

    Args:
      boxes (list of lists): A list of lists where each inner list
                             represents a box, and the indices of
                             the elements in the inner lists are
                             the keys to other boxes.

    Returns:
      bool: True if all boxes can be unlocked, False otherwise.
    """
    # Get the number of boxes.
    n = len(boxes)
    # Initialize a list to track whether each box is unlocked.
    unlocked = [False] * n
    # The first box is initially unlocked.
    unlocked[0] = True
    # Using queue we perform breadth-first search.
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            # Check if the key is within valid range.
            # and the corresponding box is not unlocked.
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)
    # Check if all boxes are unlocked
    return all(unlocked)
