# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 85-Maximal Rectangle.py
@time: 2020/12/26 10:08
@desc:

Given a rows x cols binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0


Constraints:

rows == matrix.length
cols == matrix.length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        left = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    left[i][j] = 1 if j == 0 else left[i][j - 1] + 1
        print(left)
        ret = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                width = left[i][j]
                area = width
                for k in range(i - 1, -1, -1):
                    width = min(width, left[k][j])
                    area = max(area, width * (i - k + 1))
                ret = max(ret, area)
        return ret


if __name__ == '__main__':
    s = Solution()
    ipt = [["1"]]
    print(s.maximalRectangle(ipt))
