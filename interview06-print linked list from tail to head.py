# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
#
# 示例 1：
# 输入：head = [1,3,2]
# 输出：[2,3,1]
#
# 限制：
# 0 <= 链表长度 <= 10000

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        curr = head
        values = []
        while curr is not None:
            values.insert(0, curr.val)
            curr = curr.next
        # values.reverse()
        return values