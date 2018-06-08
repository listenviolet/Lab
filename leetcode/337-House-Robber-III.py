# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root: return [0, 0]
            robLeft = dfs(root.left)
            robRight = dfs(root.right)
            norobCur = robLeft[1] + robRight[1]
            robCur = max(robLeft[0] + robRight[0] + root.val, norobCur)
            return [norobCur, robCur]
        return dfs(root)[1]

# Description:
# The thief has found himself a new place for his thievery again. 
# There is only one entrance to this area, called the "root." 
# Besides the root, each house has one and only one parent house. 
# After a tour, the smart thief realized 
# that "all houses in this place forms a binary tree". 
# It will automatically contact the police 
# if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight
# without alerting the police.

# Example 1:
#      3
#     / \
#    2   3
#     \   \ 
#      3   1
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1
# Maximum amount of money the thief can rob = 4 + 5 = 9.

# Solution:
# https://blog.csdn.net/happyaaaaaaaaaaa/article/details/50880121

# 给定到从叶子节点到第 i - 2 层抢劫的最大值 max[i-2]，
# 从叶子节点到第 i - 1 层抢劫的最大值 max[i-1]，
# 第 i 层节点的值，那么是否可以得到从叶子节点到第 i 层节点的最大值呢？
# 答案是肯定的。
# max[i] = Math.max(max[i-2]+val(a), max[i-1])。

# 这里使用递归来实现，数组rob来存储。
# rob[1]存储的是从叶子节点到当前节点抢劫的最大值，
# rob[0]存储的是从叶子节点到当前节点的左右孩子层节点抢劫到的最大值

# Note:
# 题目要求是至少隔一个偷，也就是可以隔多个偷

# Beats: 94.03%
# Runtime: 64ms
# medium