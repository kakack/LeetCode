# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 235-Lowest Common Ancestor of a Binary Search Tree.py
@time: 2020/8/14 11:28
@desc:
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

Constraints:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ## 递归
        parent_val = root.val
        if parent_val > p.val and parent_val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif parent_val < p.val and parent_val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

        ## 迭代
        parent_node = root
        while parent_node:
            if parent_node.val > p.val and parent_node.val > q.val:
                parent_node = parent_node.left
            elif parent_node.val < p.val and parent_node.val < q.val:
                parent_node = parent_node.right
            else:
                return parent_node
