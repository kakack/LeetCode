# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 637-Average of Levels in Binary Tree.py
@time: 2020/9/12 9:01 下午
@desc:
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        bfs
        """
        result = []

        nodes = collections.deque([root])
        while nodes:
            sum = 0
            n = len(nodes)
            for _ in range(n):
                node = nodes.popleft()
                sum += node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(sum / n)
        return result

    def averageOfLevels(self, root: TreeNode) -> list[float]:
        """
        :type root: TreeNode
        :rtype: List[float]
        dfs
        """
        counts, sums = [], []

        def dfs(root, depth):
            if not root:
                return
            if depth < len(counts):
                counts[depth] += 1
                sums[depth] += root.val
            else:
                sums.append(root.val)
                counts.append(1)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return [sums[i] / counts[i] for i in range(len(sums))]
