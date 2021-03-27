# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 61-Rotate List.py
@time: 2021/3/27 8:51
@desc:

Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (not head) or k == 0:
            return head
        length = 1
        cur = head
        while cur.next:
            length += 1
            cur = cur.next
        k = length - k % length
        cur.next = head
        for i in range(k):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head




