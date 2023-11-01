#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
"""

import sys


def is_safe(board, row, col):
    """ to generate range"""
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens(N):
    """ to generate chease"""
    if N < 4:
        return []

    def backtrack(col):
        if col == N:
            solutions.append(board[:])
        else:
            for row in range(N):
                if is_safe(board, row, col):
                    board[col] = row
                    backtrack(col + 1)

    board = [-1] * N
    solutions = []
    backtrack(0)
    return solutions


if __name__ == "__main__":
    """main"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print(solution)
