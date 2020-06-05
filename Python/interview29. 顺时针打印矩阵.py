# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
#  
#
# 示例 1：
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
#
# 限制：
#
# 0 <= matrix.length <= 100
# 0 <= matrix[i].length <= 100

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


