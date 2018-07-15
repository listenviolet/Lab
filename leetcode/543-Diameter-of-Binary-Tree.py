# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Max = 0
        def curSum(root):
            nonlocal Max
            if not root: return 0
            curleft, curright = 0, 0
            if root.left is not None: curleft = curSum(root.left) + 1
            if root.right is not None: curright = curSum(root.right) + 1
            # print(root.val,"curleft:",curleft,"curright",curright)
            root.val = max(curleft, curright)
            cursum = curleft + curright
            if cursum > Max: Max = cursum
            # print("cursum:", cursum, "Max:", Max)
            # print("--------------------------------------")
            return root.val
        curSum(root)
        return Max
        
# Description:
# Given a binary tree, 
# you need to compute the length of the diameter of the tree. 
# The diameter of a binary tree is the length of the longest path 
# between any two nodes in a tree. 
# This path may or may not pass through the root.

# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented 
# by the number of edges between them.


# Solution:
#                1
#              (2,3)
#             /     \
#           2        3
#         (1,2)    (0,0)
#        /     \
#       4       5  
#     (0,0)   (0,0)    

#     (i, j)
#     i = max(left + 1, right + 1) 
#       -- max(左子树最长的路径 + 1, 右子树最长的路径 + 1)
#       -- 即为当前该树最大深度
#       -- 用i值更新当前点根值
#     j = (left + 1) + (right + 1)
#       -- 左右子树最大深度之和即为经过当前根的左右子树中两点最大距离

#                         1
#                       (5,6) 
#                       /   \
#                      2     3
#                    (4,6) (0,0)
#                    /   \
#                   4     5
#                 (1,1) (3,4) 
#                  /   /    \
#                 6   7      8
#              (0,0)(2,2)  (0,0)
#                    /
#                   9
#                 (1,1) 
#                  /
#                 10
#                (0,0)

# Beats: 100.00%
# Runtime: 52ms
# easy