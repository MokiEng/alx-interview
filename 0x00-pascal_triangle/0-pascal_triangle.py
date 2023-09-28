#!/usr/bin/python3
""" a function returns a list of lists of integers representing
the Pascal’s triangle of n.
"""
def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return triangle
    else:
        for i in range(n):
            row = []
            for j in range(i + 1):
             if j == 0 or j == i:
                row.append(1)
            else:
                # Calculate the value based on the previous row
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
            triangle.append(row)

        return triangle
