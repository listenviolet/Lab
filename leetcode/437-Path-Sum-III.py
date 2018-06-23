# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    count = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def nodeSum(root):
            rootsum = []
            if root is None: return rootsum
            rootsum.append(root.val)
            if root.left is not None:
                rootsum.extend([root.val + i for i in nodeSum(root.left)])
            if root.right is not None:
                rootsum.extend([root.val + i for i in nodeSum(root.right)])
            for i in rootsum:
                if i == sum: self.count += 1
            return rootsum
        
        nodeSum(root)
        return self.count

# Description:
# You are given a binary tree 
# in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, 
# but it must go downwards 
# (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes 
# and the values are in the range -1,000,000 to 1,000,000.

# Example:

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
    
# Solution:
# 为每个节点创建一个list，
# 这个list包含所有可能的到该点的路径的sum值
#               10
#      [10,15,18,21,16,18,18]
#             /     \
#           5        -3
#     [5,8,11,6,8]   [8]   
#        /     \       \
#       3       2      11
#     [3,6,1]   [3]   [11]
#     /   \       \
#    3    -2       1
#   [3]  [-2]     [1]    

# Beats: 66.00%
# Runtime: 352ms
# easy