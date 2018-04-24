# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        Max = root.val
        def maxSum(root): 
            nonlocal Max
            if root is None: 
                return 0
            leftsum, rightsum = 0, 0
            if root.left is not None:
                leftsum = maxSum(root.left)
                if leftsum < 0:
                    leftsum = 0
            if root.right is not None:
                rightsum = maxSum(root.right)
                if rightsum < 0:
                    rightsum = 0
            Max = max(Max, root.val + leftsum + rightsum)
            return root.val + max(leftsum, rightsum)
        maxSum(root)
        return Max

# Question
# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes 
# from some starting node to any node in the tree 
# along the parent-child connections. 
# The path must contain at least one node 
# and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6
# Example 2:

# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42

# Solution:
# 如果该点为root节点，则最长路应为：
# root.val + leftsum(>=0) + rightsum(>=0)
# 若该点作为最长路径中的中间节点
# 则必然不能将左右子树全部走到
# 即只能选左右子树中的一个：最大的一个
# 这里每次递归返回的都是选好左/右子树后
# 该点作为最长路径中中间节点的值
# Max记录走到当前节点时，最长的路径
# 这里需要比较(将当前节点作为根节点，或是之前求得的Max)的最大值
# Beats: 99.23%
# hard