# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
# 字符串处理

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        res = [''] * numRows
        # 生成numRows个空字符串
        index, steps = 0, 1

        for x in s:
            res[index] += x
            if index == 0:
                steps = 1
            # 如果在第一排，那么从上往下
            elif index == numRows -1:
                steps = -1
            index += steps
            # 如果在最后一排，那么从下往上
        return ''.join(res)
        # 把字符串list整合成一个字符串