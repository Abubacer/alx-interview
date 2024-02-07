<!-- repo image -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/Abubacer/README-Template/blob/master/images/banner.png" alt="IMG" 
  </a>

<h1 align="center"></h1>
<div align="left">
<br />

# 0x05. N Queens

## Learning Objectives

At the end of this project, we are expected to be able to learn:

- Backtracking

## Requirements

  -  Allowed editors: vi, vim, emacs
  -  All files will be interpreted/compiled on Ubuntu 20.04 LTS using ```python3``` (version 3.4.3)
  -  All files should end with a new line
  -  The first line of all files should be exactly #!/usr/bin/python3
  -  A ```README.md``` file, at the root of the folder of the project, is mandatory
  -  The code should use the PEP 8 style (version 1.7.x)
  -  All files must be executable

### subhead 2
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

  - Usage: nqueens N
      - If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
  - where N must be an integer greater or equal to 4
      - If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
      - If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
  - The program should print every possible solution to the problem
      - One solution per line
      - Format: see example
      - You don’t have to print the solutions in a specific order
  - You are only allowed to import the sys module


```
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
```

</div>
