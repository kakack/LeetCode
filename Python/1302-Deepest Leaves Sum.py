# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1302-Deepest Leaves Sum.py
@time: 2020/11/3 8:50
@desc:

Given a binary tree, return the sum of values of its deepest leaves.


Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15


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
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        parents, children = [root], []
        while parents:
            sumup = 0
            for parent in parents:
                if parent.left:
                    children.append(parent.left)
                    sumup += parent.left.val
                if parent.right:
                    children.append(parent.right)
                    sumup += parent.right.val
            if not children:
                return tmp
            else:
                parents = children[:]
                children = []
                tmp = sumup
