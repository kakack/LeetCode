# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 82-Remove Duplicates from Sorted List II.py
@time: 2021/3/25 9:03
@desc:

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        vals = []
        dups = []
        cur = head
        while cur:
            if cur.val not in vals:
                vals.append(cur.val)
            elif cur.val in vals and cur.val not in dups:
                dups.append(cur.val)
            cur = cur.next
        cur_ = ListNode()
        cur_.next = head
        prehead = cur_
        while cur_.next:
            if cur_.next.val not in dups:
                cur_ = cur_.next
            else:
                cur_.next = cur_.next.next
        return prehead.next
