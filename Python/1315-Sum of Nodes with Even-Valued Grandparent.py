# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1315-Sum of Nodes with Even-Valued Grandparent.py
@time: 2020/11/19 15:59
@desc:
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.



Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.


Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def add(root):
            res = 0
            if not root or root.val % 2 != 0:
                return res
            if root.left:
                if root.left.left:
                    res += root.left.left.val
                if root.left.right:
                    res += root.left.right.val
            if root.right:
                if root.right.left:
                    res += root.right.left.val
                if root.right.right:
                    res += root.right.right.val
            return res
        def dfs(root):
            res = 0
            if root:
                res += dfs(root.left)
                res += add(root)
                res += dfs(root.right)
            return res

        ans = dfs(root)
        return ans


