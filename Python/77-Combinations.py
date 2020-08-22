# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 77-Combinations.py
@time: 2020/8/21 11:13
@desc:

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(1, k, n, [], res)
        return res

    def dfs(self, start, k, n, pre, res):
        if len(pre) == k:
            res.append(pre[:])
            return
        for i in range(start, n + 1):
            pre.append(i)
            self.dfs(i + 1, k, n, pre, res)
            pre.pop()


if __name__ == '__main__':
    n, k = 4, 2
    s = Solution()
    print(s.combine(n, k))
