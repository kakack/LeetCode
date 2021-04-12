# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 179-Largest Number.py
@time: 2021/4/12 9:05
@desc:

Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
Example 3:

Input: nums = [1]
Output: "1"
Example 4:

Input: nums = [10]
Output: "10"


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109

"""


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort(key=cmp_to_key(lambda x, y: int(str(y) + str(x)) - int(str(x) + str(y))))
        ans = ''.join([str(num) for num in nums])
        return str(int(ans))
