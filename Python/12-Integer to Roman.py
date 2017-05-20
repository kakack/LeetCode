# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.

# Subscribe to see which companies asked this question.

# 思路就是把num从大到小往下减，减掉一个往里面塞一个字符

class Solution:
    # @return a string
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        list = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                list += numerals[i]
        return list
