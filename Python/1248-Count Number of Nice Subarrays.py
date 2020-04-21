# Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.
#
# Return the number of nice sub-arrays.
#
#  
#
# Example 1:
#
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:
#
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There is no odd numbers in the array.
# Example 3:
#
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
#  
#
# Constraints:
#
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        odd = [-1]
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)
        for i in range(1, len(odd) - k):
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans
