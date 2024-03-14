#!/usr/bin/python3
"""
Determines the winner of each game played by Maria_wins and ben_wins.

Note:
 - This simulates a game where players take turns choosing prime numbers.
 - from a set of consecutive ints starting from 1 up to and including 'n'.
 - The player who cannot make a move loses the game.
 - Maria_wins always goes first and both players play optimally.

Example:
 >>> x = 3
 >>> nums = [4, 5, 1]
 >>> isWinner(x, nums)
 'Maria_wins'
"""


def isWinner(x, nums):
    """
    Determines the winner of each game played by Maria_wins and ben_wins.

    Args:
        x (int): The number of rounds played.
        nums (list): An array of ints with the value of 'n' for each round.

    Returns:
        str or None: The name of the player who won the most rounds.
                     None if the winner cannot be determined.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben_wins = 0
    maria_wins = 0

    primes = sieve_of_eratosthenes(max(nums) + 1)

    for i in nums:
        if sum(primes[:i + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    if maria_wins > ben_wins:
        return "Maria"
    return None


def sieve_of_eratosthenes(n):
    """
    Generates prime numbers using Sieve of Eratosthenes algorithm.

    Args:
        n (int): Upper limit to generate prime numbers up to.

    Returns:
        list: List of prime numbers up to 'n'.
    """
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes
