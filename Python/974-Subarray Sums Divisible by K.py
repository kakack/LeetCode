# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
#
# Example 1:
#
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#  
#
# Note:
#
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        map = [0] * K
        map[0] = 1
        preSum, count = 0, 0
        for i in range(len(A)):
            preSum = (preSum + A[i]) % K
            if preSum < 0:
                preSum += K
            count += map[preSum]
            map[preSum] += 1
        return count