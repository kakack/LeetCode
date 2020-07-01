# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 718-Maximum Length of Repeated Subarray.py
@time: 2020/7/1 9:55
@desc:
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
 

Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        def maxLength(addA, addB, length):
            ret = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        nA, nB = len(A), len(B)
        ret = 0
        for i in range(nA):
            length = min(nB, nA - i)
            ret = max(ret, maxLength(i, 0, length))
        for i in range(nB):
            length = min(nA, nB - i)
            ret = max(ret, maxLength(0, i, length))
        return ret


