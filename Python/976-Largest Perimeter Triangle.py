# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 976-Largest Perimeter Triangle.py
@time: 2020/11/29 11:41 上午
@desc:
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.



Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8


Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        n = len(A)
        for i in range(n - 1, 1, -1):
            if A[i] < (A[i - 1] + A[i - 2]):
                return A[i] + A[i - 1] + A[i - 2]
        return 0


if __name__ == '__main__':
    s = Solution()
    ipt = [1, 2, 1]
    print(s.largestPerimeter(ipt))
