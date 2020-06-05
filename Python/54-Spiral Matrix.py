# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

import sys

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directionIndex = 0
        visited = sys.maxint
        rows, columns = len(matrix), len(matrix[0])
        total = rows * columns
        ans = [0] * total
        row, col = 0, 0
        for i in range(total):
            ans[i] = matrix[row][col]
            matrix[row][col] = visited
            nextRow, nextCol = row + directions[directionIndex][0], col + directions[directionIndex][1]
            if nextRow < 0 or nextRow >= rows or nextCol < 0 or nextCol >= columns or matrix[nextRow][nextCol] == visited:
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            col += directions[directionIndex][1]
        return ans