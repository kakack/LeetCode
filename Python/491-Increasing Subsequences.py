# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 491-Increasing Subsequences.py
@time: 2020/8/25 9:21
@desc:
Given an integer array,
your task is to find all the different possible increasing subsequences of the given array,
and the length of an increasing subsequence should be at least 2.



Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]


Constraints:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates,
and two equal integers should also be considered as a special case of increasing sequence.
"""


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted(nums)
        path, result = [], []

        def recall(nums, start, path, result):
            if len(path) > 1:
                result.append(path[:])
            Hash = {}
            for i in range(start, len(nums)):
                if Hash.get(nums[i], 0):
                    continue
                elif not path:
                    path.append(nums[i])
                    Hash[nums[i]] = 1
                else:
                    if nums[i] >= path[-1]:
                        path.append(nums[i])
                        Hash[nums[i]] = 1
                    else:
                        continue
                recall(nums, i + 1, path, result)
                path.pop()

        recall(nums, 0, path, result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findSubsequences([4, 6, 7, 7]))
