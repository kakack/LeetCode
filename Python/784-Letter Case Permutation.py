# # Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Input: S = "3z4"
# Output: ["3z4", "3Z4"]

# Input: S = "12345"
# Output: ["12345"]
# Note:

# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) == 0:
            return ['']
        res = []
        sub_res = self.letterCasePermutation(S[:-1])
        for sub in sub_res:
            if S[-1].isalpha():
                res.append(sub + S[-1].lower())
                res.append(sub + S[-1].upper())
            else:
                res.append(sub + S[-1])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation('1a2b3c'))