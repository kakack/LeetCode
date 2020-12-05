# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 659-Split Array into Consecutive Subsequences.py
@time: 2020/12/5 1:50 下午
@desc:
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.



Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5
Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3, 4, 5
3, 4, 5
Example 3:

Input: [1,2,3,4,4,5]
Output: False


Constraints:

1 <= nums.length <= 10000
"""

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = collections.defaultdict(list)
        for c in nums:
            queue = counts.get(c - 1)
            if queue:
                prevLength = heapq.heappop(queue)
                heapq.heappush(counts[c], prevLength + 1)
            else:
                heapq.heappush(counts[c], 1)
        return not any(queue and queue[0] < 3 for queue in counts.values())
