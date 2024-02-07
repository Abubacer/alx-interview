#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard.

Usage examples:

./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
"""

from sys import argv, exit


def recursion_solve(row, column):
    """
    Solve the N queens problem recursively.

    Args:
        row (int): The current row being considered.
        column (int): The total number of columns on the chessboard.

    Returns:
        list: A list of valid solutions for placing queens on the chessboard.
    """
    solutions = [[]]
    for q in range(row):
        solutions = place_queen(q, column, solutions)
    return solutions


def place_queen(q, column, prev_solver):
    """
    Place a queen on the chessboard at a given row and column,
    considering previous solutions.

    Args:
        q (int): The row to place the queen in.
        column (int): The total number of columns on the chessboard.
        prev_solver (list): The list of previous solutions.

    Returns:
        list: A list of valid solutions for placing queens on the chessboard.
    """
    solver_queen = []

    for array in prev_solver:
        for x in range(column):
            if is_safe(q, x, array):
                solver_queen.append(array + [x])

    return solver_queen


def is_safe(r, c, array):
    """
    Check if it's safe to place a queen at a given row and column.

    Args:
        r (int): The row to place the queen in.
        c (int): The column to place the queen in.
        array (list): The current arrangement of queens on the chessboard.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    if c in array:
        return False
    else:
        return all(abs(array[column] - c) != r - column for column in range(r))


def get_queen_count():
    """
    Get the number of queens from command-line arguments.

    Returns:
        int: The number of queens.
    """
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    n = argv[1]

    if n.isdigit():
        return int(n)
    else:
        print("N must be a number")
        exit(1)


def init():
    """
    Initialize the N queens problem.

    Returns:
        int: The number of queens.
    """
    queen_count = get_queen_count()

    if queen_count < 4:
        print("N must be at least 4")
        exit(1)

    return queen_count


def print_solution(solution):
    """
    Format a solution for printing.

    Args:
        solution (list): A solution for placing queens on the chessboard.

    Returns:
        list: A formatted solution.
    """
    formatted_solution = []

    for q, x in enumerate(solution):
        formatted_solution.append([q, x])

    return formatted_solution


def n_queens():
    """
    Solve the N queens problem and print the solutions.
    """
    queen_count = init()

    solver = recursion_solve(queen_count, queen_count)
    for array in solver:
        formatted_solution = print_solution(array)
        print(formatted_solution)


if __name__ == '__main__':
    n_queens()
