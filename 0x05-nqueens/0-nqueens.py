#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
"""


import sys


def is_safe(board, row, col):
    """ To define range."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_solution(board):
    """ To print the solution."""
    solutions = []
    for row in board:
        queen_pos = [i for i, val in enumerate(row) if val == 1]
        solutions.append(queen_pos)
    print(solutions)


def solve_nqueens(board, col):
    """to solve the challenge."""
    if col == len(board):
        print_solution(board)
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1)
            board[i][col] = 0


def nqueens(N):
    """the N queen game."""
    if not N.isnumeric():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
