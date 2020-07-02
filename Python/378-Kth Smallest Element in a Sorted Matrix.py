# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 378-Kth Smallest Element in a Sorted Matrix.py
@time: 2020/7/2 14:47
@desc:
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.

"""
import heapq
class Solution(object):

    # 暴力排序
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        return sorted(sum(matrix, []))[k - 1]
        # n = len(matrix)
        # mat = []
        # for row in matrix:
        #     for item in row:
        #        mat.append(item)
        # mat.sort()
        # return mat[k - 1]

    # 归并排序
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)
        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
        return heapq.heappop(pq)[0]

    #
    # # 二分查找
    # def kthSmallest(self, matrix, k):
        