# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1711-Count Good Meals.py
@time: 2021/7/7 10:33
@desc:
A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

Note that items with different indices are considered different even if they have the same deliciousness value.



Example 1:

Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
Example 2:

Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.


Constraints:

1 <= deliciousness.length <= 105
0 <= deliciousness[i] <= 220
"""

from collections import Counter

class Solution(object):
    mod = 10 ** 9 + 7
    maximum = 1 << 22


    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        hashmap = Counter(deliciousness)
        ans = 0
        for x in hashmap:
            i = 1
            while i < self.maximum:
                t = i - x
                if t in hashmap:
                    if t == x:
                        ans += (hashmap[x] - 1) * hashmap[x]
                    else:
                        ans += hashmap[x] * hashmap[t]
                i <<= 1
        ans >>= 1
        return ans % self.mod

