#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given 2D matrix 90 degrees clockwise.

    Parameters:
    - matrix (list of lists): The input 2D matrix.

    Returns:
    - None (The matrix is edited in-place).
    """
    # Transpose the matrix
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
