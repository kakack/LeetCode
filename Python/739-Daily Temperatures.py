# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

# 暴力方法，逻辑是没问题，但是稳稳超时
# class Solution(object):
#     def dailyTemperatures(self, T):
#         """
#         :type T: List[int]
#         :rtype: List[int]
#         """
#         n = len(T)
#         ans = [0] * n
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if T[j] > T[i]:
#                     ans[i] = j - i
#                     break
#         return ans

# 用栈解决
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        ans = [0] * n
        stack = []
        for i in range(n):
            while len(stack) != 0 and T[i] > stack[-1][1]:
                ans[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, T[i]])
        return ans

if __name__ == '__main__':
    s = Solution()
    T = [73,74,75,71,69,72,76,73]
    print(s.dailyTemperatures(T))