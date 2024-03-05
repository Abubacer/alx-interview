#!/usr/bin/python3
"""
Calculates the perimeter of the island described in the grid.

* grid is a list of list of integers:
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally).
    - grid is rectangular, with its width and height not exceeding 100.

* The grid is completely surrounded by water.
* There is only one island (or nothing).
* The island doesn’t have “lakes” (water inside that isn’t connected
to the water surrounding the island).

Example:
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
island_perimeter(grid)  # Output: 12
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of lists of integers): the grid

    Returns:
        int: The perimeter of the island
    """
    island_perimeter = 0

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                island_perimeter += 4

                if row > 0 and grid[row - 1][col] == 1:
                    island_perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    island_perimeter -= 2

    return island_perimeter
