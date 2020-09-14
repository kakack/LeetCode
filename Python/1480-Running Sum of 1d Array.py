# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1480-Running Sum of 1d Array.py
@time: 2020/9/14 9:04
@desc:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.



Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""


class Solution:
    def runningSum(self, nums):
        if not nums:
            return []
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(res[i - 1] + nums[i])
        return res


if __name__ == '__main__':
    s = Solution()
    ipt = [1, 2, 3, 4]
    print(s.runningSum(ipt))
