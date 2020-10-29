# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 129-Sum Root to Leaf Numbers.py
@time: 2020/10/29 8:54
@desc:
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res, tmp = [], []

        def generate(tmp_):
            sum = 0
            for digit in tmp_:
                sum = sum * 10 + digit
            return sum

        def helper(root_):
            tmp.append(root_.val)
            if not root_.left and not root_.right:
                res.append(generate(tmp))
            if root_.left:
                helper(root_.left)
            if root_.right:
                helper(root_.right)
            tmp.pop()
        if root:
            helper(root)
        return sum(res)
