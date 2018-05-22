# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        if root == p or root == q: return root
        l1 = self.lowestCommonAncestor(root.left, p, q)
        l2 = self.lowestCommonAncestor(root.right, p, q)
        if l1 and l2: return root
        return l2 if l1 is None else l1

# Description
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

# Given the following binary search tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# Example 1:

# Input: root, p = 5, q = 1
# Output: 3
# Explanation: The LCA of of nodes 5 and 1 is 3.
# Example 2:

# Input: root, p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
#              according to the LCA definition.


# Solution
# 遍历判断两个node是否在左右子树中
# 若分别在左右子树中，则返回根节点
# 若均在左/右子树中，则返回左/右子树节点
# --由于递归，则返回的是距离p,q节点最近的根节点

# Beats: 24.57%
# Runtime: 147ms
# medium