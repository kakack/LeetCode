# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 812-Largest Triangle Area.py
@time: 2020/7/24 10:56
@desc:
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.

这道题给了坐标，那么明显用坐标面积公式要比海伦公式来得方便和精确。
对于三角形的坐标面积公式来说，是这样的。

    1 | x1 y1 1 |
S = - | x2 y2 1 |
​	2 | x3 y3 1 |


我们可以利用 numpy 来计算行列式的值。
利用 combiniations 来遍历所有点里任选三个点的所有组合。
也可以将行列式按照最后一列展开后，再进行运算。


"""

from itertools import combinations
import numpy as np


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        return max(
            abs(np.linalg.det(np.array([[x0, y0, 1], [x1, y1, 1], [x2, y2, 1]]))) for (x0, y0), (x1, y1), (x2, y2) in
            combinations(points, 3)) / 2


if __name__ == '__main__':
    s = Solution()
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    print(s.largestTriangleArea(points))
