# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6



class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxPillar = height.index(max(height))
        res, peakLeft, peakRight = 0, 0, len(height) - 1
        for i in range(maxPillar):
            if height[i] > height[peakLeft]:
                peakLeft = i
            else:
                res += height[peakLeft] - height[i]
        for i in range(len(height) - 1, maxPillar, -1):
            if height[i] > height[peakRight]:
                peakRight = i
            else:
                res += height[peakRight] - height[i]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))