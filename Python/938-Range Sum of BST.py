# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 938-Range Sum of BST.py
@time: 2021/4/27 9:06
@desc:
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].



Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23


Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


class Solution_(object):
    def rangeSumBST(self, root, low, high):
        res = 0
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                continue
            if node.val > high:
                q.append(node.left)
            elif node.val < low:
                q.append(node.right)
            else:
                res += node.val
                q.append(node.left)
                q.append(node.right)
        return res