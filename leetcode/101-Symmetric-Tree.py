# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        flag = 1
        
        def iter(leftroot, rightroot):
            nonlocal flag
            if flag == 0: return
            if leftroot.left is None and rightroot.right is None:
                if leftroot.right is None and rightroot.left is None:
                    return
                elif leftroot.right is None or rightroot.left is None:  
                    flag = 0
                    return
                elif leftroot.right.val != rightroot.left.val:
                    flag = 0
                    return
                elif leftroot.right.val == rightroot.left.val:
                    iter(leftroot.right, rightroot.left)
                
            elif leftroot.left is None or rightroot.right is None:
                flag = 0
                return
            elif leftroot.left.val != rightroot.right.val:
                flag = 0
                return
            elif leftroot.left.val == rightroot.right.val:
                if leftroot.right is None and rightroot.left is None:
                    iter(leftroot.left, rightroot.right)
                    return
                elif leftroot.right is None or rightroot.left is None:  
                    flag = 0
                    return
                elif leftroot.right.val != rightroot.left.val:
                    flag = 0
                    return
                elif leftroot.right.val == rightroot.left.val:
                    iter(leftroot.left, rightroot.right)
                    iter(leftroot.right, rightroot.left)
        
        if root is None: return True
        elif root.left is None and root.right is None: return True
        elif root.left is None or root.right is None: return False
        elif root.left.val != root.right.val: return False
        elif root.left.val == root.right.val:
            iter(root.left, root.right)
            if flag == 0: return False
            else: return True

# Given a binary tree, check whether it is a mirror of itself 
# (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric

# Solution:
# leftroot.left.val == rightroot.right.val
# leftroot.right.val == rightroot.left.val
# iter(leftroot.left, rightroot.right)
# iter(leftroot.right, rightroot.left)

# Note:
# Python在嵌套函数内部访问并父级函数的变量: nonlocal