<!-- repo image -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/Abubacer/README-Template/blob/master/images/banner.png" alt="IMG" 
  </a>

<h1 align="center"></h1>
<div align="left">
<br />

# 0x09. Island Perimeter 

For this project, we will need to apply our knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers. Understanding how to navigate and analyze 2D arrays and apply logical operations to determine the conditions for perimeter calculation is crucial for this task.

## Concepts Needed:



  1. 2D Arrays (Matrices):
      - Accessing and iterating over elements in a 2D array.
      - Understanding how to navigate through adjacent cells (horizontally and vertically).

  2. Conditional Logic:
      - Applying conditions to determine whether a cell contributes to the perimeter of the island.

  3. Counting Techniques:
      - Developing a method to count the edges that contribute to the island’s perimeter.

  4. Problem-Solving Strategies:
      - Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

  5. Python Programming:
      - Nested loops for iterating over grid cells.
      - Conditional statements to check the status of adjacent cells.


By thoroughly understanding these concepts and utilizing the provided resources, we will be well-prepared to tackle the coin change problem. we will need to decide whether a greedy algorithm suffices for our particular set of coin denominations or if a more comprehensive dynamic programming approach is necessary to ensure correctness and efficiency. This project not only tests algorithmic skills but also reinforces the importance of choosing the right strategy based on problem constraints.

## Learning Objectives

At the end of this project, we are expected to be able to learn:

- Island Perimeter

## Requirements

  -  Allowed editors: vi, vim, emacs
  -  All files will be interpreted/compiled on Ubuntu 20.04 LTS using ```python3``` (version 3.4.3)
  -  All files should end with a new line
  -  The first line of all files should be exactly #!/usr/bin/python3
  -  A ```README.md``` file, at the root of the folder of the project, is mandatory
  -  The code should use the PEP 8 style (version 1.7.x)
  -  All files must be executable

## Tasks

Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

  * grid is a list of list of integers:
      - 0 represents water
      - 1 represents land
      - Each cell is square, with a side length of 1
      - Cells are connected horizontally/vertically (not diagonally).
      - grid is rectangular, with its width and height not exceeding 100
  * The grid is completely surrounded by water
  * There is only one island (or nothing).
  * The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

```
guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$ 
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$ 
```

</div>
