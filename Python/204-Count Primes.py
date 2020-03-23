# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1] * n
        for i in range(2, int(math.sqrt(n)) + 1):
            if nums[i]:
                k = 2
                while k * i < n:
                    nums[k*i] = 0
                    k += 1
        res = 0
        for i in range(2, n+1):
            res += nums[i]
        return res
