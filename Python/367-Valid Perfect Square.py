# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
# Input: 16
# Output: true
#
# Example 2:
# Input: 14
# Output: false

import math

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return True if num == 0 else False
    
if __name__ == '__main__':
    s = Solution()
    for i in [1, 2, 4, 9, 16, 25, 36, 81, 124]:
        print(s.isPerfectSquare(i))