# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 90-Subsets II.py
@time: 2021/3/31 10:17
@desc:

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        l = len(nums)
        for i in range(1, l + 1):
            tmp = list(itertools.combinations(nums, i))
            for t in tmp:
                if sorted(t) not in res:
                    res.append(sorted(t))
        return res
