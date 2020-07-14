# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 59-Spiral Matrix II.py
@time: 2020/7/14 11:02
@desc:
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        matrix = [[-1] * n for _ in range(n)]
        dir, row, col = 0, 0, 0
        direction = directions[dir]
        for i in range(1, n ** 2 + 1):
            matrix[row][col] = i
            row_, col_ = row + direction[0], col + direction[1]
            if row_ >= n or col_ >= n or matrix[row_][col_] != -1:
                dir = (dir + 1) % 4
                direction = directions[dir]
                row, col = row + direction[0], col + direction[1]
            else:
                row, col = row_, col_
        return matrix

    def printMatrix(self, matrix):
        for i in matrix:
            print(i)


if __name__ == '__main__':
    s = Solution()
    s.printMatrix(s.generateMatrix(5))