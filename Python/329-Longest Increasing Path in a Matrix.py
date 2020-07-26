# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 329-Longest Increasing Path in a Matrix.py
@time: 2020/7/26 12:10 下午
@desc:
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""


import collections


class Solution(object):
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0

        rows, columns = len(matrix), len(matrix[0])
        outdegrees = [[0] * columns for _ in range(rows)]
        queue = collections.deque()
        for i in range(rows):
            for j in range(columns):
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = i + dx, j + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[i][j]:
                        outdegrees[i][j] += 1
                if outdegrees[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            ans += 1
            size = len(queue)
            for _ in range(size):
                row, column = queue.popleft()
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = row + dx, column + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] < matrix[row][
                        column]:
                        outdegrees[newRow][newColumn] -= 1
                        if outdegrees[newRow][newColumn] == 0:
                            queue.append((newRow, newColumn))

        return ans

    # DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #
    # def longestIncreasingPath(self, matrix):
    #     """
    #     :type matrix: List[List[int]]
    #     :rtype: int
    #     """
    #     if not matrix:
    #         return 0
    #     Row, Col = len(matrix), len(matrix[0])
    #
    #     def dfs(row, col):
    #         best = 1
    #         for dx, dy in Solution.DIRS:
    #             newRow, newColumn = row + dx, col + dy
    #             if 0 <= newRow < Row and 0 <= newColumn < Col and matrix[newRow][newColumn] > matrix[row][col]:
    #                 best = max(best, dfs(newRow, newColumn) + 1)
    #         return best
    #
    #     ans = 0
    #     for i in range(Row):
    #         for j in range(Col):
    #             ans = max(ans, dfs(i, j))
    #     return ans
