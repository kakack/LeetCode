# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# 画个图理解一下吧……

# 最简单的就是暴力法，枚举一遍算出最大的，但是容易超时

# 优化一点的是从左右两边朝着对方逼近，每次移动的是较短的那根，一起走到了然后算一下最大

# https://leetcode.com/articles/container-most-water/

# 1 8 6 2 5 4 8 3 7

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left, right, max_water = 0, len(height) - 1, 0
        while left < right:
            max_water = max(max_water, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water

