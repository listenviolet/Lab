# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        def postOrder(root):
            if not root: return
            postOrder(root.right)
            self.sum += root.val
            root.val = self.sum
            postOrder(root.left)
        postOrder(root)
        return root

# Description:
# Given a Binary Search Tree (BST), convert it to a Greater Tree 
# such that every key of the original BST is changed to 
# the original key plus 
# sum of all keys greater than the original key in BST.

# Example:

# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13

# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13


# Beats: 17.84%
# Runtime: 112ms
# easy