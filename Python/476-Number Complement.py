# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

# Example 1:

# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.


# Example 2:

# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


# Note:

# - The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# - You could assume no leading zero bit in the integer’s binary representation.
# - This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        def D2B(num):
            res = []
            while num > 0:
                res.append(num % 2)
                num = int(num/2)
            print(res)
            return res

        def B2D(nums):
            res = 0
            for item in reversed(nums):
                res = res * 2 + item
            print(res)
            return res

        def reverse(nums):
            res = []
            for item in nums:
                res.append(1 - item)
            print(res)
            return res

        reverseNums = D2B(num)
        comB = reverse(reverseNums)
        return B2D(comB)