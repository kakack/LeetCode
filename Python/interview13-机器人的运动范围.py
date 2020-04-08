# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#
# 示例 1：
# 输入：m = 2, n = 3, k = 1
# 输出：3
#
# 示例 2：
# 输入：m = 3, n = 1, k = 0
# 输出：1
# 提示：
# 1 <= n,m <= 100
# 0 <= k <= 20

from collections import deque
class Solution(object):
    def digitsum(self, n):
        ans = 0
        while n:
            ans += n % 10
            n //= 10
        return ans

    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        mat = [[0 for _ in range(n)] for _ in range(m)]
        mat[0][0] = 1
        temp = deque()
        temp.append([0, 0])
        res = 0

        while temp:
            temp_point = temp.popleft()
            res += 1
            x, y = temp_point
            for x_bias, y_bias in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_x = x + x_bias
                new_y = y + y_bias
                if new_x < 0 or new_x > m - 1 or new_y < 0 or new_y > n - 1 or self.digitsum(new_x) + self.digitsum(new_y) > k or mat[new_x][new_y] == 1:
                    continue
                mat[new_x][new_y] = 1
                temp.append([new_x, new_y])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(1, 2, 1))