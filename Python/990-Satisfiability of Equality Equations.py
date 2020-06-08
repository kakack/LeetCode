# Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.
#
# Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.
#
#  
#
# Example 1:
#
# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
# Example 2:
#
# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
# Example 3:
#
# Input: ["a==b","b==c","a==c"]
# Output: true
# Example 4:
#
# Input: ["a==b","b!=c","c==a"]
# Output: false
# Example 5:
#
# Input: ["c==c","b==d","x!=z"]
# Output: true
#  
#
# Note:
#
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] and equations[i][3] are lowercase letters
# equations[i][1] is either '=' or '!'
# equations[i][2] is '='


class Solution(object):
    class UnionFind:
        def __init__(self):
            self.parent = list(range(26))

        def find(self, index):
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]
        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)

    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        uf = Solution.UnionFind()
        for st in equations:
            if st[1] == '=':
                index1 = ord(st[0]) - ord('a')
                index2 = ord(st[3]) - ord('a')
                uf.union(index1, index2)
        for st in equations:
            if st[1] == '!':
                index1 = ord(st[0]) - ord('a')
                index2 = ord(st[3]) - ord('a')
                if uf.find(index1) == uf.find(index2):
                    return False
        return True
