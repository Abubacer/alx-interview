#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total

- The value of a coin will always be an integer greater than 0
- we can assume we have an infinite number of each denomination
of coin in the list
- Uses dynamic programming for efficient computation.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount.

    Args:
        coins (list of int): A list of the values of the coins in our hands.
        total (int): The target amount to reach using the coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             - If the total is 0 or less, returns 0.
             - If the total cannot be met by any number coins we have
             returns -1.
    """
    if not coins or coins is None:
        return -1

    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    change = 0

    for coin in coins:
        if coin <= 0:
            return -1

        change += total // coin
        total %= coin

    if total == 0:
        return change
    else:
        return -1
