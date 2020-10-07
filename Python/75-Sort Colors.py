# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 75-Sort Colors.py
@time: 2020/10/7 12:43 下午
@desc:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?


Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
"""


class Solution(object):
    # def sortColors(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: None Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums)
    #     ptr = 0
    #     for i in range(n):
    #         if nums[i] == 0:
    #             nums[i], nums[ptr] = nums[ptr], nums[i]
    #             ptr += 1
    #     for i in range(ptr, n):
    #         if nums[i] == 1:
    #             nums[i], nums[ptr] = nums[ptr], nums[i]
    #             ptr += 1

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        i, head, tail = 0, 0, n - 1
        while i <= tail:
            if nums[i] == 0:
                nums[i], nums[head] = nums[head], nums[i]
                head += 1
            elif nums[i] == 2:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail -= 1
                i -= 1
            i += 1
        return


if __name__ == '__main__':
    s = Solution()
    ipt = [2,0,2,1,1,0]
    s.sortColors(ipt)
    print(ipt)

