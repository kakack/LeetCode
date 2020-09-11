# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 216-Combination Sum III.py
@time: 2020/9/11 11:02
@desc:
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution(object):


    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []

        def dfs(num, sum, tmp):
            if len(tmp) > k or sum > n:
                return
            if len(tmp) == k and sum == n:
                self.result.append(tmp[:])
                return
            for i in range(num + 1, 10):
                if sum + i > n:
                    break
                dfs(i, sum + i, tmp + [i])

        dfs(0, 0, [])
        return self.result


if __name__ == '__main__':
    s = Solution()
    # print(s.combinationSum3(3, 7))
    # print(s.combinationSum3(3, 9))
    print(s.combinationSum3(3, 2))
