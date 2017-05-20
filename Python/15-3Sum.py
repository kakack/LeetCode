# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        res = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                target = 0 - nums[i] - nums[j]
                if target in nums[j+1:]:
                    res.append((nums[i], nums[j], target))
        return list(set(res))

# 这个办法容易超时

