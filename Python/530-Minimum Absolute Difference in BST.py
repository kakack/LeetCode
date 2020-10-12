# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 530-Minimum Absolute Difference in BST.py
@time: 2020/10/12 9:08
@desc:
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).


Note:

There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""

import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
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
