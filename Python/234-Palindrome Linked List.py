# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
# Input: 1->2
# Output: false

# Example 2:
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        deque = []
        curr = head
        while curr is not None:
            deque.append(curr.val)
            curr = curr.next
        first, second = 0, len(deque) - 1
        while first < second:
            if deque[first] != deque[second]:
                return False
            else:
                first += 1
                second -= 1
        return True
