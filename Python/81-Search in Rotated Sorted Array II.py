# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 81-Search in Rotated Sorted Array II.py
@time: 2021/4/7 4:41 下午
@desc:

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.



Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104


Follow up: This problem is the same as Search in Rotated Sorted Array, where nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        length = len(nums)
        if length == 1:
            return nums[0] == target
        front, end = 0, length - 1
        while front <= end:
            mid = (front + end) // 2
            if nums[mid] == target:
                return True
            if nums[front] == nums[mid] and nums[mid] == nums[end]:
                front += 1
                end -= 1
            elif nums[front] <= nums[mid]:
                if nums[front] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    front = mid + 1
            else:
                if nums[mid] < target and target <= nums[length - 1]:
                    front = mid + 1
                else:
                    end = mid - 1

        return False
