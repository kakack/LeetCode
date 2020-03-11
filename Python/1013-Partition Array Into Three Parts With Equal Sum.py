# Given
# an
# array
# A
# of
# integers,
# return true if and only if we
# can
# partition
# the
# array
# into
# three
# non - empty
# parts
# with equal sums.
#
# Formally, we
# can
# partition
# the
# array if we
# can
# find
# indexes
# i + 1 < j
# with (A[0] + A[1] + ... + A[i] == A[i + 1] + A[i + 2] + ... + A[j - 1] == A[j] + A[j - 1] + ... + A[A.length - 1])
#
# Example1:
# Input: A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#
# Example 2:
# Input: A = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
# Output: false

# Example 3:
# Input: A = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
# Constraints:
#
# 3 <= A.length <= 50000
# -10 ^ 4 <= A[i] <= 10 ^ 4

class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sumA = sum(A)
        if sumA % 3 != 0:
            return False
        else:
            target = int(sumA / 3)
        subSum = 0
        first = -1
        second = -2
        for i in range(len(A)):
            subSum += A[i]
            if subSum == target:
                first = i
                break
        subSum = 0
        for i in range(len(A)-1, -1, -1):
            subSum += A[i]
            if subSum == target:
                second = i
                break
        return True if first < second - 1 else False