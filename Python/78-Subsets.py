# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 78-Subsets.py
@time: 2020/9/6 1:06 下午
@desc:
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        递归
        """
        n = len(nums)
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        回溯
        """



if __name__ == '__main__':
    s = Solution()
    ipt = [1, 2, 3, 4, 5]
    print(s.subsets(ipt))
