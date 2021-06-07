# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 494-Target Sum.py
@time: 2021/6/7 11:22
@desc:
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.



Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1


Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""


# class Solution(object):
#     count = 0
#
#     def backtrack(self, nums, target, index, sum):
#         if index == len(nums):
#             if sum == target:
#                 self.count += 1
#         else:
#             self.backtrack(nums, target, index + 1, sum + nums[index])
#             self.backtrack(nums, target, index + 1, sum - nums[index])
#
#     def findTargetSumWays(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         self.backtrack(nums, target, 0, 0)
#         return self.count


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sum = 0
        for num in nums:
            sum += num
        diff = sum - target
        if diff < 0 or diff % 2 != 0:
            return 0
        neg = diff / 2
        dp = [0] * (neg + 1)
        dp[0] = 1
        for num in nums:
            for j in range(neg, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[neg]
