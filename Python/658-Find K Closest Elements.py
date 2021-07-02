# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 658-Find K Closest Elements.py
@time: 2021/7/2 16:39
@desc:
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        idx = 0
        res = []
        if x <= arr[0]:
            idx = 0
        elif x >= arr[-1]:
            idx = len(arr) - 1
        else:
            for index in range(len(arr) - 1):
                if arr[index] == x:
                    idx = index
                    break
                elif arr[index] < x and arr[index + 1] > x:
                    idx = index if arr[index + 1] - x >= x - arr[index] else index + 1
        k -= 1
        res.append(arr[idx])
        left, right = idx - 1, idx + 1
        print(idx, left, right)
        while k:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1
            elif x - arr[left] > arr[right] - x:
                res.append(arr[right])
                right += 1
            elif x - arr[left] <= arr[right] - x:
                res.append(arr[left])
                left -= 1
            print(left, right, res)
            k -= 1
        return sorted(res)


if __name__ == '__main__':
    s = Solution()
    # print(s.findClosestElements([1, 2, 3, 4, 5], 4, -1))
    # print(s.findClosestElements([1, 2, 3, 4, 5], 4, 3))
    # print(s.findClosestElements([-2, -1, 1, 2, 3, 4, 5], 7, 3))
    print(s.findClosestElements([0, 1, 2, 2, 2, 3, 6, 8, 8, 9], 5, 9))
