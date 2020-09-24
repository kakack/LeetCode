# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 501-Find Mode in Binary Search Tree.py
@time: 2020/9/24 9:33
@desc:
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import Counter


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return

        inorderRes, res = [], []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inorderRes.append(root.val)
            inorder(root.right)

        inorder(root)
        d = dict(Counter(inorderRes))
        m = max(d.values())
        for k, v in d.items():
            if v == m:
                res.append(k)
        return res


if __name__ == '__main__':
    ipt = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
    res, most, count, base = [], 0, 0, ipt[0]
    for i in ipt:
        if i == base:
            count += 1
        else:
            if count == most:
                res.append[base]
            elif count > most:
                res = [base]
                most = count
            base = i
            count = 1
    print(res)
