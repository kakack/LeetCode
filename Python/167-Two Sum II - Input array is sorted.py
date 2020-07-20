# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 167-Two Sum II - Input array is sorted.py
@time: 2020/7/20 9:45
@desc:
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i, j = 0, n - 1
        while i < j:
            target_ = numbers[i] + numbers[j]
            if target_ == target:
                return i + 1, j + 1
            elif target_ > target:
                j -= 1
            elif target_ < target:
                i += 1
        return None


if __name__ == '__main__':
    s = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(numbers, target))

