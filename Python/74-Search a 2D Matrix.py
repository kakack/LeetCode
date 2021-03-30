# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 74-Search a 2D Matrix.py
@time: 2021/3/30 9:42
@desc:

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[rows - 1][cols - 1]:
            return False
        beginRow, endRow = 0, rows - 1
        row, col = 0, 0
        while beginRow <= endRow:
            row = (endRow + beginRow) >> 1
            if target < matrix[row][0]:
                endRow = row - 1
            elif target > matrix[row][cols - 1]:
                beginRow = row + 1
            else:
                break
        beginCol, endCol = 0, cols - 1
        while beginCol <= endCol:
            col = (endCol + beginCol) >> 1
            if target < matrix[row][col]:
                endCol = col - 1
            elif target > matrix[row][col]:
                beginCol = col + 1
            else:
                break
        return target == matrix[row][col]


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    s = Solution()
    s.searchMatrix(matrix, target)
