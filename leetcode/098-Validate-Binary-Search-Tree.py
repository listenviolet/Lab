# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        tree = []

        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            tree.append(root.val)
            inorder(root.right)

        inorder(root)
        if len(tree) == 0 or len(tree) == 1:
            return True
        for i in range(0, len(tree) - 1):
            if(tree[i] >= tree[i + 1]):
                return False
        return True

# Use inorder : small - med - large

# Note that in python recursion, 
# "return" only return current recursion result
# can not end the whole recursion