# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1295-Find Numbers with Even Number of Digits.py
@time: 2020/10/23 9:08
@desc:
Given an array nums of integers, return how many of them contain an even number of digits.


Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.


Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def count(num):
            res = 0
            while num > 0:
                res += 1
                num = num // 10
            return res % 2 == 0

        res = 0
        for num in nums:
            if count(num):
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    # ipt = [12, 345, 2, 6, 7896]
    ipt = [555, 901, 482, 1771]
    print(s.findNumbers(ipt))
