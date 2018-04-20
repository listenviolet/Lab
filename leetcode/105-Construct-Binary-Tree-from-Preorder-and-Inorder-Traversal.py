# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return None
        root = preorder[0]
        index = inorder.index(root)
        lefttree = []
        righttree = []
        if index > 0 : lefttree = inorder[0: index]
        if index < len(inorder) - 1: righttree = inorder[index + 1:]
        
        pre_lefttree = []
        if index > 0: pre_lefttree = preorder[1:index + 1]
        pre_righttree = []
        if index < len(preorder) - 1: pre_righttree = preorder[index + 1:]
        
        t = TreeNode(root)
        
        t.left = self.buildTree(pre_lefttree, lefttree)
        t.right = self.buildTree(pre_righttree, righttree)
        
        return t
            
# Question
# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#    3
#   / \
#  9  20
#    /  \
#   15   7     

# Solution:
# preorder 的第一个元素一定是树的根值
# 在inorder中找到其索引值index
# 则inorder中下标小于index的元素集合构成该树的左子树
# inorder中下标大于index的元素集合构成该树的右子树
# 每次返回（子）树的根节点，链接到大树左右孩子
# 返回根节点即可
# beats 40.73%