# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 113-Path Sum II.py
@time: 2020/9/26 9:21 下午
@desc:
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

import collections


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        Depth-First-Search
        """
        cur, res = [], []

        def dfs(root, sum):
            if not root:
                return
            cur.append(root.val)
            if not root.left and not root.right and sum == root.val:
                res.append(cur)
            dfs(root.left, sum - root.val)
            dfs(root.right, sum - root.val)
            cur.pop()

        dfs(root, sum)
        return res

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        Breadth-First-Search
        """
        res = []
        parent = collections.defaultdict(lambda: None)

        def getPath(node):
            tmp = list()
            while node:
                tmp.append(node.val)
                node = parent[node]
            res.append(tmp[::-1])

        if not root:
            return res
        que_node = collections.deque([root])
        que_total = collections.deque([0])

        while que_node:
            node = que_node.popleft()
            rec = que_total.popleft() + node.val
            if not node.left and not node.right:
                if rec == sum:
                    getPath(node)
            else:
                if node.left:
                    parent[node.left] = node
                    que_node.append(node.left)
                    que_total.append(rec)
                if node.right:
                    parent[node.right] = node
                    que_node.append(node.right)
                    que_total.append(rec)
        return res



