# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution:
    def maxProduct(self, nums):
        prodi = 0
        res = float('-inf')
        for i in range(len(nums)):
            if prodi == 0:
                prodi = 1
                pos = 1
                neg = 1
            prodi *= nums[i]
            res = max(res, prodi/pos) if prodi > 0 else max(res, prodi / neg)
            if prodi > 0 and abs(pos) > abs(prodi):
                pos = prodi
            if prodi < 0 and (abs(neg) > abs(prodi) or neg > 0):
                neg = prodi
        return int(res)
