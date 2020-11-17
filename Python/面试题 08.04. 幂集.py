# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 面试题 08.04. 幂集.py
@time: 2020/11/17 10:44
@desc:
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

说明：解集不能包含重复的子集。

示例:

 输入： nums = [1,2,3]
 输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


# 非递归
class Solution1(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            n = len(res)
            for i in range(n):
                temp = list(res[i])
                temp.append(num)
                res.append(temp)
        return res


# 回溯
"""
private void backtrack("原始参数") {
    //终止条件(递归必须要有终止条件)
    if ("终止条件") {
        //一些逻辑操作（可有可无，视情况而定）
        return;
    }

    for (int i = "for循环开始的参数"; i < "for循环结束的参数"; i++) {
        //一些逻辑操作（可有可无，视情况而定）

        //做出选择

        //递归
        backtrack("新的参数");
        //一些逻辑操作（可有可无，视情况而定）

        //撤销选择
    }
}

"""


class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()

        def backtrack(res, tempList, nums, start):
            res.append(list(tempList))
            for i in range(start, len(nums)):
                tempList.append(nums[i])
                backtrack(res, tempList, nums, i + 1)
                tempList.pop(-1)

        backtrack(res, [], nums, 0)
        return res


# 位运算法
class Solution3(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = 1 << len(nums)
        res = []
        for i in range(length):
            tmp = list()
            for j in range(len(nums)):
                if i >> j & 1 == 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res


if __name__ == '__main__':
    s = Solution3()
    ipt = [1, 2, 3]
    print(s.subsets(ipt))
