# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 925-Long Pressed Name.py
@time: 2020/10/21 11:12
@desc:
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.


Constraints:

1 <= name.length <= 1000
1 <= typed.length <= 1000
The characters of name and typed are lowercase letters.
"""


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        n, m = len(name), len(typed)
        i, j = 0, 0
        if name[0] != typed[0] or name[-1] != typed[-1]:
            return False
        while i < n and j < m:
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if typed[j - 1] == typed[j]:
                    j += 1
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    # name = "alex"
    # typed = "aaleex"
    name = "pyplrz"
    typed = "ppyypllr"
    if s.isLongPressedName(name, typed):
        print("True")
    else:
        print("False")


