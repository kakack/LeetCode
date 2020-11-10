# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 31-Next Permutation.py
@time: 2020/11/10 9:23
@desc:
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                for j in range(n - 1, i - 1, -1):
                    if nums[j] > nums[i]:
                        break
                nums[i], nums[j] = nums[j], nums[i]
                nums[i+1:] = list(reversed(nums[i+1:]))
                return
        nums[:] = list(reversed(nums[:]))
        return

