# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 783-Minimum Distance Between BST Nodes.py
@time: 2021/4/13 10:10
@desc:
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys


class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        :type root: TreeNode
        :rtype: int
        """
        vals = []

        def dfs(root):
            if root:
                dfs(root.left)
                vals.append(root.val)
                dfs(root.right)

        dfs(root)
        minDiff = sys.maxsize
        for i in range(len(vals) - 1):
            minDiff = min(minDiff, abs(vals[i + 1] - vals[i]))
        return minDiff
