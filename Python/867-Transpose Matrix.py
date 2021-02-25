# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 867-Transpose Matrix.py
@time: 2021/2/25 9:03
@desc:
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.





Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
"""

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(matrix), len(matrix[0])

        ans = [[None] * n for _ in range(m)]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans
