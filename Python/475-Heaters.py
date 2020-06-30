# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 475-Heaters.py
@time: 2020/6/30 18:59
@desc:
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.


Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.


Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""

import bisect


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        res = []
        heaters.sort()
        houses.sort()
        nheaters, nhouses = len(heaters), len(houses)
        for house in houses:
            index = bisect.bisect_left(heaters, house)
            left, right = max(0, index - 1), min(nheaters - 1, index)
            if left == right:
                res.append(abs(house - heaters[left]))
            else:
                res.append(min(house - heaters[index - 1], heaters[index] - house))
        return max(res)


        """
        [1,2,3]
        [2]
        [1,2,3,4]
        [1,4]
        [1,2,3,5,15]
        [2,30]
        """


if __name__ == '__main__':
    houses1 = [1, 2, 3]
    heaters1 = [2]
    houses2 = [1, 2, 3, 4]
    heaters2 = [1, 4]
    houses3 = [1, 2, 3, 5, 15]
    heaters3 = [2, 30]
    s = Solution()
    print(s.findRadius(houses1, heaters1))
    print(s.findRadius(houses2, heaters2))
    print(s.findRadius(houses3, heaters3))