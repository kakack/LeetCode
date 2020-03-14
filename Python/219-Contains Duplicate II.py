# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
#
# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashMap = {}
        for i, item in enumerate(nums):
            if hashMap.get(item) is not None:
                if (i - hashMap[item]) <= k:
                    return True
            hashMap[item] = i
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(s.containsNearbyDuplicate([1,0,1,1], 1))
    print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))
