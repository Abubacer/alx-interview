#!/usr/bin/python3
"""
Determines the winner of each game played by Maria and Ben.

Note:
 - This simulates a game where players take turns choosing prime numbers.
 - from a set of consecutive ints starting from 1 up to and including 'n'.
 - The player who cannot make a move loses the game.
 - Maria always goes first and both players play optimally.

Example:
 >>> x = 3
 >>> nums = [4, 5, 1]
 >>> isWinner(x, nums)
 'Maria'
"""


def isWinner(x, nums):
    """
    Determines the winner of each game played by Maria and Ben.

    Args:
        x (int): The number of rounds played.
        nums (list): An array of ints with the value of 'n' for each round.

    Returns:
        str or None: The name of the player who won the most rounds.
                     None if the winner cannot be determined.
    """
    def isPrime(n):
        """
        Checks if n is a prime number

        Args:
            n (int): The number to check.

        Returns:
            bool: True if 'n' is prime, False otherwise.
        """
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def gamePlay(n):
        """
        Determines the winner of a single round of the game

        Args:
            n (int): The number of rounds played.

        Returns:
            str: The name of the player who won the round.
        """
        if n == 1:
            return "Ben"
        if n % 2 == 0:
            return "Maria"
        else:
            return "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        isWinner = gamePlay(n)
        if isWinner == "Maria":
            maria_wins += 1
        elif isWinner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
