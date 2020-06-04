# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
# Example:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        def char_in_row(char):
            row = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
            for i in range(3):
                if char in row[i]:
                    return i
        ans_, ans = [], []
        for word in words:
            index = -1
            for c in word:
                c = c.lower()
                if index < 0:
                    index = char_in_row(c)
                elif index != char_in_row(c):
                    ans_.append(word)
                    break
        for word_ in words:
            if word_ not in ans_:
                ans.append(word_)
        return ans

if __name__ == '__main__':
    s = Solution()
    input = ["Hello", "Alaska", "Dad", "Peace"]
    print(s.findWords(input))