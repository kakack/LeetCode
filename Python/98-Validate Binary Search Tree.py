# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#  
#
# Example 1:
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # if root is None:
        #     return True
        # if root.left is None and root.right is None:
        #     return True
        # elif root.left is None and root.right:
        #     return root.val < root.right.val and self.isValidBST(root.right)
        # elif root.left and root.right is None:
        #     return root.left.val < root.val and self.isValidBST(root.left)
        # else:
        #     return root.left.val < root.val < root.right.val and self.isValidBST(root.left) and self.isValidBST(root.right)
        def judge(root, lower=float("-inf"), upper=float("inf")):
            if not root:
                return True
            val = root.val
            if val <= lower or val >= upper:
                return False
            if not judge(root.left, lower, val):
                return False
            if not judge(root.right, val, upper):
                return False
            return True
        return judge(root)
