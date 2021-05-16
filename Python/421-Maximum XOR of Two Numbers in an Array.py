# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 421-Maximum XOR of Two Numbers in an Array.py
@time: 2021/5/16 3:27 下午
@desc:

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?



Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [0]
Output: 0
Example 3:

Input: nums = [2,4]
Output: 6
Example 4:

Input: nums = [8,10,2]
Output: 10
Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127


Constraints:

1 <= nums.length <= 2 * 104
0 <= nums[i] <= 231 - 1

"""


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x, high_bit = 0, 30
        for k in range(high_bit, -1, -1):
            seen = set()
            for num in nums:
                seen.add(num >> k)
            x_next = x * 2 + 1
            found = False
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break
            if found:
                x = x_next
            else:
                x = x_next - 1
        return x



