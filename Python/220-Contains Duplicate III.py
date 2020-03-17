# Given an array of integers,
# find out whether there are two distinct indices i and j in the array
# such that the absolute difference between nums[i] and nums[j] is at most t
# and the absolute difference between i and j is at most k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true

# Example 3:
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        hashMap = {}
        for i, item in enumerate(nums):
            for value in hashMap:
            # for value in range(item - t, item + t + 1):
            #     index = hashMap.get(value)
                index = hashMap.get(value)
                if abs(value - item) <= t and abs(index - i) <= k:
                    return True
            hashMap[item] = i
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyAlmostDuplicate([2,1], 1, 1))
    print(s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
    print(s.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
    print(s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
