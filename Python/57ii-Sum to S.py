# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

#  

# 示例 1：

# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
# 示例 2：

# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#  

# 限制：

# 1 <= target <= 10^5


class Solution(object):
    def isAdded(self, target, num):
        res = []
        if (2 * target + num + num * num) % (2 * num) == 0:
            first = int((2 * target + num - num * num) / (2 * num))
            for i in range(num):
                res.append(first + i)
            return res

    def underTarget(self, target, num):
        if ((1 + num) * num)/2 <= target:
            return True
        else:
            return False

    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if target in [1, 2]:
            return res

        for i in range(2, int(target/2)):
            if self.underTarget(target, i):
                r = self.isAdded(target, i)
                if r is not None:
                    res.insert(0, r)
            else:
                break
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findContinuousSequence(15))