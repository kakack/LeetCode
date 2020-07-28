# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 104-Maximum Depth of Binary Tree.py
@time: 2020/7/28 8:43
@desc:
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        # if root.right is None and root.left is None:
        #     return 1
        # elif root.right is None:
        #     return self.maxDepth(root.left) + 1
        # elif root.left is None:
        #     return self.maxDepth(root.right) + 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1