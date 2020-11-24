# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 222-Count Complete Tree Nodes.py
@time: 2020/11/24 9:11
@desc:
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def countNodes(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     count = 0
    #     def dfs(root):
    #         nonlocal count
    #         if root:
    #             dfs(root.left)
    #             count += 1
    #             dfs(root.right)
    #     dfs(root)
    #     return count

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def exist(root, height, k):
            bit = 1 << (height - 1)
            cur = root
            while cur and bit > 0:
                if not (bit & k):
                    cur = cur.left
                else:
                    cur = cur.right
                bit >>= 1
            return cur

        if not root:
            return 0
        height = 0
        cur = root
        while cur.left:
            height += 1
            cur = cur.left
        low = 1 << height
        high = (1 << (height + 1)) - 1
        while low < high:
            mid = (high - low + 1) // 2 + low
            if exist(root, height, mid):
                low = mid
            else:
                high = mid - 1
        return low

