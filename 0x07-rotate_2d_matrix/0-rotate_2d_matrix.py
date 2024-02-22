#!/usr/bin/python3
"""
Rotates an n x n 2D matrix 90 degrees clockwise.

Example:
    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ]
    >>> rotate_2d_matrix(matrix)
    >>> print(matrix)
    [[7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]]
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise.

    Args:
        matrix (list): A 2D matrix.

    Returns:
        None: The matrix is rotated in-place. No return value.
    """
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row of the transposed matrix
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
