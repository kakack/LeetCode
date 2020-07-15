# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 96-Unique Binary Search Trees.py
@time: 2020/7/15 9:55
@desc:
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0 for _ in range(n + 1)]
        res[0], res[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                res[i] += res[j - 1] * res[i - j]
        return res[n]
        # def helper(n):
        #     if n in [0, 1]:
        #         return 1
        #     ans = 0
        #     for i in range(1, n + 1):
        #         ans += helper(i - 1) * helper(n - i)
        #     return ans
        # return helper(n)

        


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(3))

