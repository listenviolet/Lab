from hashlib import md5
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def tuplify(root):
            return (root.val, tuplify(root.left), tuplify(root.right)) if root else None
        return str(tuplify(t)) in str(tuplify(s))

# Description:
# Given two non-empty binary trees s and t, 
# check whether tree t has exactly the same structure 
# and node values with a subtree of s. 
# A subtree of s is a tree consists of a node in s 
# and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.

# Example 1:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure 
# and node values with a subtree of s.
# Example 2:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.

# Solution:
# 把树结构转换为前序遍历表示的字符串形式
# 查找子树结构则变成了查找子字符串

# Beats: 92.45%
# Runtime: 92ms
# easy