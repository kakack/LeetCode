# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = ListNode(-1)
        pre.next = head
        curr, end = pre, pre
        for i in range(n):
            end = end.next

        while end and end.next:
            curr = curr.next
            end = end.next
        if n != 1:
            curr.next = curr.next.next
        else:
            curr.next = None
        return pre.next