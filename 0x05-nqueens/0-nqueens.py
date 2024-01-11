#!/usr/bin/python3
import sys
"""
chess queen
"""


def is_safe(board, row, col, n):
    """
    Check if it is safe to place a queen in the given
    position on the board.
    """
    for i in range(row):
        if board[i][col] == 1 or \
           (col - row + i >= 0 and board[i][col - row + i] == 1) or \
           (col + row - i < n and board[i][col + row - i] == 1):
            return False
    return True


def solve_nqueens_util(board, row, n, solutions):
    """
    Recursively solve the N-Queens problem and store
    solutions in the 'solutions' list.
    """

    if row == n:
        solutions.append([[i, board[i].index(1)] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row][col] = 0


def solve_nqueens(n):
    """
    Solve the N-Queens problem for the given board size.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
