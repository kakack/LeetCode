# -*- coding: utf-8 -*

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return 1
        nums.sort()
        max_len, len_ = 0, 1
        pre = nums[0]
        for item in nums[1:]:
            if item - 1 == pre:
                len_ += 1
            elif item != pre:
                len_ = 1
            max_len = max(max_len, len_)
            pre = item
        return max_len

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,0,1]
    print(s.longestConsecutive(nums))