# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    Max = 0
    len = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Max = 0

        def dfs(root, len):
            nonlocal Max
            if root is None:
                return
            len = len + 1
            if len > Max:
                Max = len
            dfs(root.left, len)
            dfs(root.right, len)

        dfs(root, 0)
        return Max

# Question:
# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its depth = 3.
