# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
#
#  
#
# 示例 1:
#
# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
#  
#
# 提示：
#
# 0 <= num < 231

# class Solution(object):
#     def translateNum(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         nums = str(num)
#         def dfs(nums, pointer):
#             if pointer >= len(nums) - 1:
#                 return 1
#             tmp = int(nums[pointer] + nums[pointer + 1])
#             if tmp >= 10 and tmp <= 25:
#                 return dfs(nums, pointer + 1) + dfs(nums, pointer + 2)
#             else:
#                 return dfs(nums, pointer + 1)
#         return dfs(nums, 0)

class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = str(num)
        n = len(nums)
        memo = [0] * (n + 1)
        memo[n - 1], memo[n] = 1, 1
        def dfs(nums, pointer, memo):
            if memo[pointer] > 0:
                return memo[pointer]
            tmp = int(nums[pointer] + nums[pointer + 1])
            if tmp >= 10 and tmp <= 25:
                memo[pointer] = dfs(nums, pointer + 1, memo) + dfs(nums, pointer + 2, memo)
            else:
                memo[pointer] = dfs(nums, pointer + 1, memo)
            return memo[pointer]
        return dfs(nums, 0, memo)