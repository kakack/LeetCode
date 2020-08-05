# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 337-House Robber III.py
@time: 2020/8/5 10:15
@desc:
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def rob_(root):
            if not root:
                return 0, 0
            ls, ln = rob_(root.left)
            rs, rn = rob_(root.right)
            # ls表示偷左子树能带来的最大收益，ln表示不偷左子树能带来的最大收益，rs、rn同理
            return root.val + ln + rn, max(ls, ln) + max(rs, rn)
        return max(rob_(root))
