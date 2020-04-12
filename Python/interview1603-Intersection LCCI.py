# Given two straight line segments (represented as a start point and an end point), compute the point of intersection, if any. If there's no intersection, return an empty array.
#
# The absolute error should not exceed 10^-6. If there are more than one intersections, return the one with smallest X axis value. If there are more than one intersections that have same X axis value, return the one with smallest Y axis value.
# Example 1:
#
# Input:
# line1 = {0, 0}, {1, 0}
# line2 = {1, 1}, {0, -1}
# Output:  {0.5, 0}
# Example 2:
#
# Input:
# line1 = {0, 0}, {3, 3}
# line2 = {1, 1}, {2, 2}
# Output:  {1, 1}
# Example 3:
#
# Input:
# line1 = {0, 0}, {1, 1}
# line2 = {1, 0}, {2, 1}
# Output:  {}  (no intersection)
# Note:
#
# The absolute value of coordinate value will not exceed 2^7.
# All coordinates are valid 2D coordinates.

class Solution:
    def intersection(self, start1, end1, start2, end2):
        """
        :type start1: List[int]
        :type end1: List[int]
        :type start2: List[int]
        :type end2: List[int]
        :rtype: List[float]
        """
        x1, y1, x2, y2, x3, y3, x4, y4 = float(start1[0]), float(start1[1]), float(end1[0]), float(end1[1]), float(start2[0]), float(start2[1]), float(end2[0]), float(end2[1])
        det = lambda a, b, c, d: a * d - b * c
        d = det(x1 - x2, x4 - x3, y1 - y2, y4 - y3)
        p = det(x4 - x2, x4 - x3, y4 - y2, y4 - y3)
        q = det(x1 - x2, x4 - x2, y1 - y2, y4 - y2)
        if d != 0:
            lam, eta = p / d, q / d
            if not (0 <= lam <= 1 and 0 <= eta <= 1): return []
            return [lam * x1 + (1 - lam) * x2, lam * y1 + (1 - lam) * y2]
        if p != 0 or q != 0: return []
        t1, t2 = sorted([start1, end1]), sorted([start2, end2])
        if t1[1] < t2[0] or t2[1] < t1[0]: return []
        return max(t1[0], t2[0])