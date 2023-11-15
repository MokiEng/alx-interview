#!/usr/bin/python3
"""2D matrix rotation module."""


def rotate_2d_matrix(matrix):
    """ rotate 90 degrees clockwise an n x n 2D matrix."""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
