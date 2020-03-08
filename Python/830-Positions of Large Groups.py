# In a string S of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

# The final answer should be in lexicographic order.


# Example 1:

# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
# Example 2:

# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# Example 3:

# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]


# Note:  1 <= S.length <= 1000


class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        count = 0
        res = []
        pre = ''
        for i in range(len(S)):
            if S[i] == pre:
                count += 1
            else:
                if count >= 3:
                    res.append([i - count, i - 1])
                count = 1
            pre = S[i]
        if count >= 3:
            res.append([len(S) - count, len(S) - 1])
        return res

        # count, maxCount = 0, 0
        # res = []
        # pre = ''
        # for i in range(len(S)):
        #     if S[i] == pre:
        #         count += 1
        #         if count == maxCount:
        #             res.append([i - count + 1, i])
        #         elif count > maxCount:
        #             res.clear()
        #             res.append([i - count + 1, i])
        #             maxCount = count
        #     else:
        #         count = 1
        #     pre = S[i]
        # return res


if __name__ == '__main__':
    s = Solution()
    print(s.largeGroupPositions("abbxxxxzzy"))
    print(s.largeGroupPositions("abc"))
    print(s.largeGroupPositions("abcdddeeeeaabbbcd"))
    print(s.largeGroupPositions("aaa"))
    print(s.largeGroupPositions("bcdaaaa"))