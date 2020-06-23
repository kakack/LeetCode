# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 414-Third Maximum Number.py
@time: 2020/6/23 9:52 下午
@desc:
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

"""

import sys
class Solution(object):
    stack = []
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.stack = [-sys.maxint - 1] * 3
        def updateStack(n):
            for i in range(3):
                if n > self.stack[i]:
                    self.stack.insert(i, n)
                    self.stack.pop()
                    break

        for num in nums:
            if num > self.stack[-1] and num not in self.stack:
                updateStack(num)
        return self.stack[-1] if self.stack[-1] != -sys.maxint - 1 else self.stack[0]


if __name__ == '__main__':
    s = Solution()
    # print(s.thirdMax([3, 2, 1]))
    print(s.thirdMax([1, 2]))
    # print(s.thirdMax([2, 2, 3, 1]))

