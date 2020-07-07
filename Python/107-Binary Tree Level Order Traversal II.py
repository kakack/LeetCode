# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 107-Binary Tree Level Order Traversal II.py
@time: 2020/7/7 10:36
@desc:
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res, cur = [], []
        if not root:
            return []
        else:
            cur.append(root)
            res.insert(0, [root.val])
        while len(cur) != 0:
            child, child_val = [], []
            for node in cur:
                if node.left:
                    child.append(node.left)
                    child_val.append(node.left.val)
                if node.right:
                    child.append(node.right)
                    child_val.append(node.right.val)
            if len(child_val) > 0:
                res.insert(0, child_val)
            cur[:] = child[:]
        return res

