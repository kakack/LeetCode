# A popular masseuse receives a sequence of back-to-back appointment requests and is debating which ones to accept. She needs a break between appointments and therefore she cannot accept any adjacent requests. Given a sequence of back-to-back appoint­ ment requests, find the optimal (highest total booked minutes) set the masseuse can honor. Return the number of minutes.
#
# Note: This problem is slightly different from the original one in the book.
#
# Example 1:
#
# Input:  [1,2,3,1]
# Output:  4
# Explanation:  Accept request 1 and 3, total minutes = 1 + 3 = 4
# Example 2:
#
# Input:  [2,7,9,3,1]
# Output:  12
# Explanation:  Accept request 1, 3 and 5, total minutes = 2 + 9 + 1 = 12
# Example 3:
#
# Input:  [2,1,4,5,3,1,1,3]
# Output:  12
# Explanation:  Accept request 1, 3, 5 and 8, total minutes = 2 + 4 + 3 + 3 = 12

class Solution:
    def massage(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        dp0, dp1 = 0, nums[0]
        for i in range(1, n):
            tdp0 = max(dp0, dp1)  # 计算 dp[i][0]
            tdp1 = dp0 + nums[i]  # 计算 dp[i][1]
            dp0, dp1 = tdp0, tdp1

        return max(dp0, dp1)
