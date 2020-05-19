# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(leftTree, rightTree):
            if leftTree is None:
                return rightTree is None
            elif rightTree is None:
                return leftTree is None
            elif leftTree.val != rightTree.val or not isSym(leftTree.left, rightTree.right) or not isSym(leftTree.right, rightTree.left):
                return False
            else:
                return True

        if not root:
            return True
        else:
            return isSym(root.left, root.right)