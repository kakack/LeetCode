# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for rowNum in range(numRows):
            row = [None for _ in range(rowNum + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, rowNum):
                row[j] = triangle[rowNum - 1][j - 1] + triangle[rowNum - 1][j]
            triangle.append(row)
        return triangle

if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))