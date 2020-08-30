# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 283-Move Zeroes.py
@time: 2020/8/30 12:01 下午
@desc:
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        for i in range(count):
            nums.remove(0)
        print(nums)
        nums += [0 for _ in range(count)]


if __name__ == '__main__':
    # ipt = [0, 1, 0, 3, 12]
    ipt = [0, 0, 0, 0, 3, 0, 0, 0, 10, 0, 0, 0]
    s = Solution()
    s.moveZeroes(ipt)
    print(ipt)
