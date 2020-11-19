# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 283-Move Zeroes.py
@time: 2020/11/19 9:32
@desc:
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         count = nums.count(0)
#         for i in range(count):
#             nums.remove(0)
#         print(nums)
#         nums += [0 for _ in range(count)]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: x == 0)
        print(nums)
        # return nums


if __name__ == '__main__':
    s = Solution()
    ipt = [0, 1, 0, 3, 12]
    s.moveZeroes(ipt)
