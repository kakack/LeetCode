# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: interview  Offer 11-旋转数组的最小数字.py
@time: 2020/7/22 9:35
@desc:
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

"""
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2
            if numbers[mid] < numbers[r]:
                r = mid
            elif numbers[mid] > numbers[r]:
                l = mid + 1
            else:
                r -= 1
        return numbers[l]


if __name__ == '__main__':
    nums = [3, 4, 5, 6, 7, 1, 2]
    s = Solution()
    print(s.minArray(nums))