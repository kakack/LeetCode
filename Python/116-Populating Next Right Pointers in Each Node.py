# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 116-Populating Next Right Pointers in Each Node.py
@time: 2020/10/15 9:28
@desc:
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        leftnode = root
        while leftnode.left:
            head = leftnode
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftnode = leftnode.left
        return root

    # def connect(self, root):
    #     """
    #     :type root: Node
    #     :rtype: Node
    #     """
    #
    #     def process(root):
    #         if not root:
    #             return
    #         if root.left:
    #             root.left.next = root.right
    #         if root.right and root.next:
    #             root.right.next = root.next.left
    #         process(root.left)
    #         process(root.right)
    #
    #     process(root)
    #     return root
