# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 993-Cousins in Binary Tree.py
@time: 2021/5/17 10:23
@desc:
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

"""

import collections


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        parent_x, depth_x, found_x = None, None, False
        parent_y, depth_y, found_y = None, None, False

        def dfs(node, depth, parent):
            if not node:
                return
            nonlocal parent_x, depth_x, found_x, parent_y, depth_y, found_y
            if node.val == x:
                parent_x, depth_x, found_x = parent, depth, True
            elif node.val == y:
                parent_y, depth_y, found_y = parent, depth, True
            if found_x and found_y:
                return
            dfs(node.left, depth + 1, node)
            if found_x and found_y:
                return
            dfs(node.right, depth + 1, node)

        dfs(root, 0, None)
        return depth_x == depth_y and parent_x != parent_y

    def isCousins_(self, root, x, y):
        parent_x, depth_x, found_x = None, None, False
        parent_y, depth_y, found_y = None, None, False

        def update(node, parent, depth):
            if node.val == x:
                nonlocal parent_x, depth_x, found_x
                parent_x, depth_x, found_x = parent, depth, True
            elif node.val == y:
                nonlocal parent_y, depth_y, found_y
                parent_y, depth_y, found_y = parent, depth, True

        q = collections.deque([(root, 0)])
        update(root, None, 0)
        while q:
            node, depth = q.popleft()
            if node.left:
                q.append((node.left, depth + 1))
                update(node.left, node, depth + 1)
            if node.right:
                q.append((node.right, depth + 1))
                update(node.right, node, depth + 1)
            if found_x and found_y:
                break
        return depth_x == depth_y and parent_x != parent_y
