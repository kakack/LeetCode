# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 117-Populating Next Right Pointers in Each Node II.py
@time: 2020/9/28 9:45
@desc:
Given a binary tree

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

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
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

        def getDepth(root):
            if not root:
                return 0
            elif not root.left and not root.right:
                return 1
            else:
                return 1 + max(getDepth(root.left), getDepth(root.right))

        depth = getDepth(root)
        levels = [[] for _ in range(depth)]

        def travel(root, i):
            if not root:
                return
            else:
                levels[i].append(root)
                travel(root.left, i + 1)
                travel(root.right, i + 1)

        travel(root, 0)
        for i in range(len(levels)):
            for j in range(len(levels[i]) - 1):
                levels[i][j].next = levels[i][j + 1]
        return root

# class Solution(object):
#     def connect(self, root):
#         """
#         :type root: Node
#         :rtype: Node
#         """
#         head = root
#         while head:
#             cur = head
#             pre = head = None
#             while cur:
#                 if cur.left:
#                     if not pre:
#                         pre = head = cur.left
#                     else:
#                         pre.next = cur.left
#                         pre = pre.next
#                 if cur.right:
#                     if not pre:
#                         pre = head = cur.right
#                     else:
#                         pre.next = cur.right
#                         pre = pre.next
#                 cur = cur.next
#         return root
