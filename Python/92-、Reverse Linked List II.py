# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 92-、Reverse Linked List II.py
@time: 2021/3/18 9:25
@desc:
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        def reverse(head, n):
            pre = tail = head
            for i in range(1, n):
                tail = tail.next
            pretail = tail.next
            while pre != tail:
                tmp = pre.next
                pre.next = pretail
                pretail = pre
                pre = tmp
            tail.next = pretail
            return tail

        pr = head
        if left == right:
            return head
        elif left == 1:
            return reverse(head, right)
        else:
            for i in range(1, left - 1):
                pr = pr.next
            pr.next = reverse(pr.next, right - left + 1)
            return head
