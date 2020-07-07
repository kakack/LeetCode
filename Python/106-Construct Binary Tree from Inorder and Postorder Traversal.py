# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 106-Construct Binary Tree from Inorder and Postorder Traversal.py
@time: 2020/7/7 11:17
@desc:
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def help(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)

            index = idx_map[val]
            root.right = help(index + 1, in_right)
            root.left = help(in_left, index - 1)
            return root

        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return help(0, len(inorder) - 1)