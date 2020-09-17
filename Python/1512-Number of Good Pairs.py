# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1512-Number of Good Pairs.py
@time: 2020/9/17 8:38
@desc:
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0
        if n <= 1:
            return 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    res += 1

        return res


if __name__ == '__main__':
    s = Solution()
    # ipt = [1, 2, 3, 1, 1, 3]
    ipt = [1, 2, 3]
    print(s.numIdenticalPairs(ipt))
