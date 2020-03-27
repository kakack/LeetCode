# Given two arrays arr1 and arr2, the elements of arr2 are distinct,
# and all elements in arr2 are also in arr1.
#
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
# Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
#
# Example 1:
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
#
# Constraints:
# - arr1.length, arr2.length <= 1000
# - 0 <= arr1[i], arr2[i] <= 1000
# - Each arr2[i] is distinct.
# - Each arr2[i] is in arr1.


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr2dict = {}
        rest = []
        res = []
        for item in arr2:
            arr2dict[item] = 0
        for item in arr1:
            if arr2dict.get(item) is not None:
                arr2dict[item] += 1
            else:
                rest.append(item)
        for item in arr2:
            while arr2dict[item] > 0:
                res.append(item)
                arr2dict[item] -= 1
        rest.sort()
        return res + rest

if __name__ == '__main__':
    s = Solution()
    print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))