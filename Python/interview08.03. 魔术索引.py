# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: interview08.03. 魔术索引.py
@time: 2020/7/31 10:04
@desc:

魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。

示例1:

 输入：nums = [0, 2, 3, 4, 5]
 输出：0
 说明: 0下标的元素为0
示例2:

 输入：nums = [1, 1, 1]
 输出：1
提示:

nums长度在[1, 1000000]之间
"""


class Solution(object):
    # def findMagicIndex(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     for i in range(len(nums)):
    #         if nums[i] == i:
    #             return i
    #     return -1
    def findMagicIndex(self, nums):
        def getMethod(nums, left, right):
            if left > right:
                return -1
            mid = (right - left) // 2 + left
            leftAnswer = getMethod(nums, left, mid - 1)
            if leftAnswer != -1:
                return leftAnswer
            elif nums[mid] == mid:
                return mid
            else:
                return getMethod(nums, mid + 1, right)
        return getMethod(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.findMagicIndex([0, 2, 3, 4, 5]))
