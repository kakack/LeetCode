# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        row = [""] * min(numRows, len(s))
        curRow = 0
        goingDown = False

        for c in s:
            row[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            if goingDown:
                curRow += 1
            else:
                curRow -= 1
        res = ''
        for st in row:
            res += st
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))