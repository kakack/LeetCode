# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 47-Permutations II.py
@time: 2020/9/18 8:22 下午
@desc:
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(left, history):
            nonlocal res
            if not left:
                res.append(history)
            for i in set(left):
                left.remove(i)
                left.append(i)
                backtrack(left[:-1], history + [i])

        backtrack(nums, [])
        return res


if __name__ == '__main__':
    s = Solution()
    ipt = [1, 1, 2]
    print(s.permuteUnique(ipt))
