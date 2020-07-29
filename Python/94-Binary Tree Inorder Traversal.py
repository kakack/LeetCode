# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 94-Binary Tree Inorder Traversal.py
@time: 2020/7/29 9:50
@desc:
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def travel(root_):
            if root_ is None:
                return
            else:
                travel(root_.left)
                res.append(root_.val)
                travel(root_.right)

        travel(root)
        return res
