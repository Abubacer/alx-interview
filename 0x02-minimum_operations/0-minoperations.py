#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste.

Given a number n, minOperations() is a method that calculates the
fewest number of operations needed to result in exactly n H characters
in the file.

Example:
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste
=> HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """
    Calculates the minimum number of operations
    needed to achieve the desired number of 'H' in the file.

    Parameters:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
             Or 0 if n is impossible to achieve.
    """
    # check if n is impossible to achieve
    if n < 1:
        return 0

    numbers_operations = 0
    divisor = 2

    # n factorization and opeerations
    while n > 1:
        while n % divisor == 0:
            # perform the "Copy All" operation
            numbers_operations += divisor
            # Perform the "Paste" operation p-1 times
            n //= divisor
        # check the next number for being a prime factor
        divisor += 1

    return numbers_operations
