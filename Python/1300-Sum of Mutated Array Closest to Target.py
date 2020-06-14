# # -*- coding: utf-8 -*
#
# Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.
#
# In case of a tie, return the minimum such integer.
#
# Notice that the answer is not neccesarilly a number from arr.
#
#  
#
# Example 1:
#
# Input: arr = [4,9,3], target = 10
# Output: 3
# Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
# Example 2:
#
# Input: arr = [2,3,5], target = 10
# Output: 5
# Example 3:
#
# Input: arr = [60864,25176,27249,21296,20204], target = 56803
# Output: 11361
#  
#
# Constraints:
#
# 1 <= arr.length <= 10^4
# 1 <= arr[i], target <= 10^5

class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        if n == 0:
            return 0
        arr.sort()
        sum = 0
        for i in range(n):
            x = (target - sum) / (n - i)

            if x < arr[i]:
                y = float(target - sum) / (n - i)
                if y - x > 0.5:
                    return x + 1
                else:
                    return x
            sum += arr[i]
        return  arr[n - 1]