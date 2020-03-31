# Given an array of integers nums, sort the array in ascending order.
#
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
#
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
#
# Constraints:
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000

class Solution(object):
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(1, n - i):
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return nums

    def insertionSort(self, nums):
        n = len(nums)
        for i in range(1, n):
            while i> 0 and nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                i -= 1
        return nums


    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # return self.selectionSort(nums)
        # return self.bubbleSort(nums)
        return self.insertionSort(nums)
#         nums.sort()


if __name__ == '__main__':
    s = Solution()
    nums = [5,1,1,2,0,0]
    print(s.sortArray(nums))