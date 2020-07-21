# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 95-Unique Binary Search Trees II.py
@time: 2020/7/21 9:46
@desc:
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


Constraints:

0 <= n <= 8
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateTree(start, end):
            if start > end:
                return [None]
            allTrees = []
            for i in range(start, end + 1):
                leftSubTree = generateTree(start, i - 1)
                rightSubTree = generateTree(i + 1, end)
                for l in leftSubTree:
                    for r in rightSubTree:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            return allTrees
        return generateTree(1, n) if n else []

