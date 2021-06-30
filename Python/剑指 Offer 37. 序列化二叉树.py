# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 剑指 Offer 37. 序列化二叉树.py
@time: 2021/6/30 14:38
@desc:
请实现两个函数，分别用来序列化和反序列化二叉树。

你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

 

示例：


输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if not root:
                return [None]
            else:
                return [root.val] + dfs(root.left) + dfs(root.right)
        return str(dfs(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        dataArray = eval(data)
        def dfs(data1):
            root_val = dataArray.pop(0)
            if root_val == None:
                return None
            root = TreeNode(root_val)
            root.left = dfs(data1)
            root.right = dfs(data1)
            return root
        return dfs(dataArray)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))