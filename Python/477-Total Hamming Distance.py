# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 477-Total Hamming Distance.py
@time: 2021/5/28 9:57
@desc:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.



Example 1:

Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Example 2:

Input: nums = [4,14,4]
Output: 4


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109

nums中所有元素二进制的第i位共有c个1，n-c个0，那么这些元素在第i位上的汉明距离之和为c*(n-c)
具体实现时，对于整数val 二进制的第 i 位，我们可以用代码 (val >> i) & 1 来取出其第 i 位的值。
此外，由于 10^9 < 2^30，我们可以直接从二进制的第 0 位枚举到第 29位。

"""


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans
