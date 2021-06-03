# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 525-Contiguous Array.py
@time: 2021/6/3 11:15
@desc:
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.



Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        MaxLength, counter, n = 0, 0, len(nums)
        mp = {0: -1}
        for i in range(n):
            num = nums[i]
            if num == 1:
                counter += 1
            else:
                counter -= 1
            if counter in mp.keys():
                prevIndex = mp[counter]
                MaxLength = max(MaxLength, i - prevIndex)
            else:
                mp[counter] = i
        return MaxLength
