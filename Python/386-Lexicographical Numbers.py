# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 386-Lexicographical Numbers.py
@time: 2020/11/2 9:38
@desc:
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space.
The input size may be as large as 5,000,000.
"""


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []

        def dfs(cur):
            if cur > n:
                return
            res.append(cur)
            for i in range(10):
                dfs(cur * 10 + i)

        for i in range(1, 10):
            dfs(i)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.lexicalOrder(13))
