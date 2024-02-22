<!-- repo image -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/Abubacer/README-Template/blob/master/images/banner.png" alt="IMG" 
  </a>

<h1 align="center"></h1>
<div align="left">
<br />

# 0x07. Rotate 2D Matrix

For this project, we are tasked with implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python. Below are the key concepts and resources that we need to grasp in order to successfully complete this project.

By understanding these concepts and utilizing the provided resources, we will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests our ability to manipulate 2D matrices but also challenges us to think about optimizing our solution to operate in-place, thus improving our problem-solving and algorithmic thinking skills in Python.

Concepts Needed:

  1. Matrix Representation in Python:
      - Understanding how 2D matrices are represented using lists of lists in Python.
      - Accessing and modifying elements in a 2D matrix.

  2. In-place Operations:
      - Performing operations on data without creating a copy of the data structure.
      - The importance of minimizing space complexity by modifying the matrix in place.

  3. Matrix Transposition:
      - Understanding the concept of transposing a matrix (swapping rows and columns).
      - Implementing matrix transposition as a step in the rotation process.

  4. Reversing Rows in a Matrix:
      - Manipulating rows of a matrix by reversing their order as part of the rotation process.

  5. Nested Loops:
      - Using nested loops to iterate through 2D data structures like matrices.
      - Modifying elements within nested loops to achieve the desired rotation.


## Learning Objectives

At the end of this project, we are expected to be able to learn:

- Rotate an n x n 2D matrix by 90 degrees clockwise.

## Requirements

  -  Allowed editors: vi, vim, emacs
  -  All files will be interpreted/compiled on Ubuntu 20.04 LTS using ```python3``` (version 3.4.3)
  -  All files should end with a new line
  -  The first line of all files should be exactly #!/usr/bin/python3
  -  A ```README.md``` file, at the root of the folder of the project, is mandatory
  -  The code should use the PEP 8 style (version 1.7.x)
  -  All files must be executable

## Tasks
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

  - Prototype: def rotate_2d_matrix(matrix):
  - Do not return anything. The matrix must be edited in-place.
  - You can assume the matrix will have 2 dimensions and will not be empty.

```
jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$
```

</div>
