# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return None
        root = TreeNode(postorder[-1])
        ind = inorder.index(root.val)
        
        left_in, right_in, left_post, right_post = [], [], [], []
        
        if ind > 0: 
            left_in = inorder[: ind]
            left_post = postorder[: ind]
            
        if ind + 1 < len(inorder): 
            right_in = inorder[ind + 1:]
            right_post = postorder[ind: -1]

        root.left = self.buildTree(left_in, left_post)
        root.right = self.buildTree(right_in, right_post)
        return root

# Description:
# Given inorder and postorder traversal of a tree, 
# construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# Solution
# 后序中，最后一个点为树的根节点，
# 以此根值在中序中找到ind, ind左边为左子树部分，右边为右子树部分，
# 再以同样方法，构造子树。

# Beats: 10.61%
# Runtime: 364ms
# medium