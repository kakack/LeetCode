# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 3
# Output: [1,3,3,1]

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        cur = 1
        ans.append(cur)
        for i in range(1,rowIndex + 1):
            cur = int(cur * (rowIndex - i + 1)/i)
            ans.append(cur)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))

