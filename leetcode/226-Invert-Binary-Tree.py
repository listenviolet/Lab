# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root is None: return
        # if root.left is None or root.right is None: return root
        temp = root.right
        root.right = root.left
        root.left = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Description
# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Solution:
# 注意有只有左/右子树也可以invert

# Beats: 99.43%
# Runtime: 36ms
# easy