# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 114-Flatten Binary Tree to Linked List.py
@time: 2020/8/2 9:36 上午
@desc:
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def flatten(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: None Do not return anything, modify root in-place instead.
    #     """
    #     if root is None:
    #         return None
    #     preOrder = []
    #     def preTravel(root):
    #         if root:
    #             preOrder.append(root)
    #             preTravel(root.left)
    #             preTravel(root.right)
    #     preTravel(root)
    #     n = len(preOrder)
    #     for i in range(1, n):
    #         prev, curr = preOrder[i - 1], preOrder[i]
    #         prev.left = None
    #         prev.right = curr


    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr
