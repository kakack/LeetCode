# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def trans(l):
            res = 0
            count = 0
            while l is not None:
                res += l.val * (10 ** count)
                l = l.next
                count += 1
            return res

        def rebuild(num):
            if num == 0:
                return ListNode(0)
            head = ListNode(0)
            curr = head
            while num > 0:
                curr.next = ListNode(num % 10)
                curr = curr.next
                num = num // 10
            return head.next

        l1_val, l2_val = trans(l1), trans(l2)
        return rebuild(l1_val + l2_val)

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         carry = 0
#         root = n = ListNode(0)
#         while l1 or l2 or carry:
#             v1 = v2 = 0
#             if l1:
#                 v1 = l1.val
#                 l1 = l1.next
#             if l2:
#                 v2 = l2.val
#                 l2 = l2.next
#             carry, val = divmod(v1+v2+carry, 10)
#             n.next = n = ListNode(val)
#         return root.next