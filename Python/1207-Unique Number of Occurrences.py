# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1207-Unique Number of Occurrences.py
@time: 2020/10/28 9:29
@desc:
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.



Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true


Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

import collections


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = collections.Counter(arr).values()
        for count in collections.Counter(counts).values():
            if count != 1:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    ipt = [26, 2, 16, 16, 5, 5, 26, 2, 5, 20, 20, 5, 2, 20, 2, 2, 20, 2, 16, 20, 16, 17, 16, 2, 16, 20, 26, 16]
    print(s.uniqueOccurrences(ipt))
