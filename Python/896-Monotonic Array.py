# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 896-Monotonic Array.py
@time: 2021/2/28 1:32 下午
@desc:
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        start = 1
        increase = True
        while start < len(A):
            if A[start] == A[start - 1]:
                start += 1
                continue
            elif A[start] > A[start - 1]:
                break
            else:
                increase = False
                break
        for i in range(start, len(A)):
            if A[i] == A[i - 1]:
                continue
            elif increase != (A[i] > A[i - 1]):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    ipts = [[1, 2, 2, 3],
            [6, 5, 4, 4],
            [6],
            [1, 2, 3, 4, 4, 3, 2, 1],
            [1, 2, 3, 4, 4, 3, 5, 6]]
    for ipt in ipts:
        print(s.isMonotonic(ipt))
