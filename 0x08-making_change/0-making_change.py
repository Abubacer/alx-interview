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
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    min_coins_needed = [float('inf')] * (total + 1)
    min_coins_needed[0] = 0  # Base case: 0 coins needed to make total of 0

    for coin in coins:
        for j in range(coin, total + 1):
            min_coins_needed[j] = min(
                min_coins_needed[j],
                min_coins_needed[j - coin] + 1
                )

    # If total cannot be met by any number coins we have, return -1
    if min_coins_needed[total] != float('inf'):
        return min_coins_needed[total]
    else:
        return -1
