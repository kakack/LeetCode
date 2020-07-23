# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 60-Permutation Sequence.py
@time: 2020/7/23 10:30
@desc:
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from itertools import permutations
        # 构造[1,2,3,4....n]
        list_n = list(range(n + 1))
        list_n.pop(0)
        # 构造全排列list
        arr = list(permutations(list_n))
        # 返回第k个
        return ''.join(map(str, list(arr[k - 1])))


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(3, 3))
    print(s.getPermutation(4, 9))
