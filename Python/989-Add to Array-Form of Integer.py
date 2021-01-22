# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 989-Add to Array-Form of Integer.py
@time: 2021/1/22 9:46
@desc:
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.



Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000


Note：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
If A.length > 1, then A[0] != 0
"""

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        listK, ans = [], []
        while K > 0:
            listK.insert(0, K % 10)
            K = K // 10
        if len(A) > len(listK):
            listK = [0] * (len(A) - len(listK)) + listK
        elif len(A) < len(listK):
            A = [0] * (len(listK) - len(A)) + A
        c, n = 0, len(A)
        for i in range(n - 1, -1, -1):
            tmp = listK[i] + A[i] + c
            c = tmp // 10
            ans.insert(0, tmp % 10)
        if c:
            ans.insert(0, c)
        return ans
        

