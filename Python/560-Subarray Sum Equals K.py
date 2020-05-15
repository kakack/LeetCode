# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
#
# Input:nums = [1,1,1], k = 2
# Output: 2
#  
#
# Constraints:
#
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

import collections
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # count = 0
        # for start in range(len(nums)):
        #     sum = 0
        #     for end in reversed(range(start + 1)):
        #         sum += nums[end]
        #         if sum == k:
        #             count += 1
        # return count

        num_times = collections.defaultdict()
        num_times[0] = 1
        cur_sum = 0
        res = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - k in num_times:
                res += num_times[cur_sum - k]
            num_times[cur_sum] = num_times.get(cur_sum, 0) + 1
        return res




