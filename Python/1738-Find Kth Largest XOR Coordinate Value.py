# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1738-Find Kth Largest XOR Coordinate Value.py
@time: 2021/5/19 9:46
@desc:
You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

Find the kth largest value (1-indexed) of all the coordinates of matrix.



Example 1:

Input: matrix = [[5,2],[1,6]], k = 1
Output: 7
Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
Example 2:

Input: matrix = [[5,2],[1,6]], k = 2
Output: 5
Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.
Example 3:

Input: matrix = [[5,2],[1,6]], k = 3
Output: 4
Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.
Example 4:

Input: matrix = [[5,2],[1,6]], k = 4
Output: 0
Explanation: The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0, which is the 4th largest value.


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 106
1 <= k <= m * n
"""


class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        result = list()
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] ^ pre[i][j - 1] ^ pre[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                result.append(pre[i][j])
        result.sort(reverse=True)
        return result[k - 1]

