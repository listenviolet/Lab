# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def findMostRight(root):
            if root.right is not None:
                return findMostRight(root.right)
            elif root.left is not None:
                return findMostRight(root.left)
            else: return root
        
        while root is not None:
            if root.left is not None:  
                mostright = findMostRight(root.left)
                mostright.right = root.right
                root.right = root.left
                root.left = None
                root = root.right
            elif root.right is not None: 
                root = root.right
            else: break

# Given a binary tree, flatten it to a linked list in-place.

# For example, given the following tree:

#    1
#   / \
#  2   5
# / \   \
#3   4   6
#The flattened tree should look like:

#1
# \
#  2
#   \
#    3
#     \
#      4
#       \
#        5
#         \
#          6

# Solution: 实现将树中所有左子树转为右子树
# 1. 若有左子树，则应将其转为右子树：
#    先找到左子树的最右节点，
#    然后将根节点的右子树连接到左子树的最右节点的右孩子
#    然后将整个左子树作为根节点的右子树
#    注意，之后要将根节点的左子树赋值为None

# 2. 若无左子树，则应继续遍历，看右子树的孩子是否有左子树
# 3. 当根节点没有左右子树时，结束循环