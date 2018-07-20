class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """    
        def mergeSub(t1, t2):
            if t1.left is not None and t2.left is not None:
                t1.left.val += t2.left.val
                mergeSub(t1.left, t2.left)
            if t1.left is None and t2.left is not None:
                t1.left = t2.left
            
            if t1.right is not None and t2.right is not None:
                t1.right.val += t2.right.val
                mergeSub(t1.right, t2.right)
            if t1.right is None and t2.right is not None:
                t1.right = t2. right
        
        if t1 is not None and t2 is not None:
            t1.val += t2.val
            mergeSub(t1, t2)
        if t1 is None and t2 is not None:
            t1 = t2
        return t1

# Description:
# Given two binary trees and imagine that 
# when you put one of them to cover the other, 
# some nodes of the two trees are overlapped 
# while the others are not.

# You need to merge them into a new binary tree. 
# The merge rule is that if two nodes overlap, 
# then sum node values up as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of new tree.

# Example 1:
# Input: 
#     Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
#          3
#         / \
#        4   5
#       / \   \ 
#      5   4   7
# Note: 
# The merging process must start from the root nodes of both trees.

# Solution:
# 合并节点的值到t1的树中：
# t1   t2
# 其中t1是已经与t2加和的节点
# 若t1.left is None and t2.left is not None: 直接将t2.left拼接过来
# 若t1.left != None and t2.left != None : 
# 节点加和, mergeSub(t1.left,t2.left)
# 若t1.left != None and t2.left is None : 不变
# 若t1.left is None and t2.left is None : 不变

# right的同理

# Beats: 81.39%
# Runtime: 96ms
# easy