# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 66-Plus One.py
@time: 2020/7/29 14:35
@desc:
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        if n == 0:
            return [1]
        carry, idx = 1, n - 1
        while carry != 0 and idx >= 0:
            carry, digits[idx] = (digits[idx] + carry) // 10, (digits[idx] + carry) % 10
            print(digits[idx], carry)
            idx -= 1
        if idx == -1 and carry == 1:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    s = Solution()
    # print(s.plusOne([1, 2, 3]))
    # # print(s.plusOne([4, 3, 2, 1]))
    print(s.plusOne([9, 9, 9, 9]))
