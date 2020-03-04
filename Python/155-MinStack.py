# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


# Example:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

from collections import deque

# class MinStack(object):
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.origin = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         self.origin.append(x)
#
#     def pop(self):
#         """
#         :rtype: None
#         """
#         self.origin.pop()
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.origin[len(self.origin) - 1]
#
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return min(self.origin)


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.origin = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.origin.append(x)
        if 0 == len(self.min) or x <= self.min[len(self.min) - 1]:
            self.min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        i = self.origin.pop()
        if i == self.min[len(self.min) - 1]:
            self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.origin[len(self.origin) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[len(self.min) - 1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()