# -*- coding: utf-8 -*

"""
@author: Kai Chen
@file: 203-Remove Linked List Elements.py
@time: 2020/6/19 10:54
@desc:
"""

# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        sentinel.next = head

        pre, cur = sentinel, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return sentinel.next
