# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 1232-Check If It Is a Straight Line.py
@time: 2021/1/17 5:27 下午
@desc:
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.


"""


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        n = len(coordinates)
        if n <= 2:
            return True
        pre = 1
        if coordinates[1][0] == coordinates[0][0]:
            for i in range(2, n):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
            return True
        slop = float(coordinates[1][1] - coordinates[0][1]) / float(coordinates[1][0] - coordinates[0][0])
        for i in range(2, n):
            if coordinates[i][0] - coordinates[pre][0] == 0:
                return False
            if slop == float(coordinates[i][1] - coordinates[pre][1]) / float(coordinates[i][0] - coordinates[pre][0]):
                pre = i
                continue
            else:
                return False
        return True
