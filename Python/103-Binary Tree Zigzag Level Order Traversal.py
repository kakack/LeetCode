# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 103-Binary Tree Zigzag Level Order Traversal.py
@time: 2020/12/22 9:32
@desc:
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        def bfs(rt, level):
            if rt is None:
                return
            if level > len(result):
                result.append([])
            if level % 2 == 1:
                result[level - 1].append(rt.val)
            else:
                result[level - 1].insert(0, rt.val)
            bfs(rt.left, level + 1)
            bfs(rt.right, level + 1)

        bfs(root, 1)
        return result
