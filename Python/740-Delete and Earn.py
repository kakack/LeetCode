# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 740-Delete and Earn.py
@time: 2021/5/5 3:51 下午
@desc:
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.



Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points.
6 total points are earned.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
"""


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = max(nums)
        total = [0] * (maxVal + 1)
        for val in nums:
            total[val] += val

        def rob(nums):
            size = len(nums)
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, size):
                first, second = second, max(first + nums[i], second)
            return second

        return rob(total)
