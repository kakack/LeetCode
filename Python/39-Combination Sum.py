# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 39-Combination Sum.py
@time: 2020/7/17 9:20
@desc:
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        if n == 0:
            return []
        candidates.sort()
        path, res = [], []
        self.dfs(candidates, 0, n, path, res, target)
        return res

    def dfs(self, candidates, begin, size, path, res, target):
        if target == 0:
            res.append(path[:])
            return
        for index in range(begin, size):
            resideue = target - candidates[index]
            if resideue < 0:
                break
            path.append(candidates[index])
            self.dfs(candidates, index, size, path, res, resideue)
            path.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    s = Solution()
    print(s.combinationSum(candidates, target))