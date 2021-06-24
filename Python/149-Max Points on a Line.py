# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 149-Max Points on a Line.py
@time: 2021/6/24 10:24
@desc:
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.



Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
Accepted
"""
import collections


class Solution(object):
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 2:
            return n
        ret = 0
        for i in range(n):
            if ret >= n - i or ret > n / 2:
                break
            mp = collections.defaultdict(int)
            for j in range(i + 1, n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if x == 0:
                    y = 1
                elif y == 0:
                    x = 1
                else:
                    if y < 0:
                        x = -x
                        y = -y
                    gcdXY = self.gcd(abs(x), abs(y))
                    x = x / gcdXY
                    y = y / gcdXY
                mp[y + x * 20001] += 1
            maxn = 0
            for num in mp.values():
                maxn = max(maxn, num + 1)
            ret = max(ret, maxn)
        return ret


class Solution_(object):
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 2:
            return n
        ret = 1
        for i in range(n):
            mp = collections.defaultdict(int)
            pi = points[i]
            for j in range(n):
                if i != j:
                    pj = points[j]
                    dx = pj[0] - pi[0]
                    dy = pj[1] - pi[1]
                    gcd = self.gcd(abs(dx), abs(dy))
                    sir = str(dy / gcd) + ':' + str(dx / gcd)
                    mp[sir] += 1
                    ret = max(ret, mp[sir] + 1)
        return ret


if __name__ == '__main__':
    points = [[1, 1], [2, 2], [3, 3]]
    s = Solution()
    print(s.maxPoints(points))
