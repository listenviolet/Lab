# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q1 = []
        q2 = []
        front, rear = 0, 0
        level1, level2 = 0, 0
        
        if root is None: return q2
        
        subq = []
        subq.append(root.val)
        q1.append(root)
        #q2.append(subq)
        rear = rear + 1
        level1 = rear
        level2 = rear
        subq = []
        while(front < rear):
            
            
            cur = q1[front]
            subq.append(cur.val)
            front = front + 1
            
            if front == level1:
                if subq: q2.append(subq)
                subq = []
                
            if cur.left is not None: 
                q1.append(cur.left)
                #subq.append(cur.left.val)
                rear = rear + 1
                
            if cur.right is not None: 
                #subq.append(cur.right.val)
                q1.append(cur.right)
                rear = rear + 1 
            
            level2 = rear
            
            if front == level1:
                level1 = level2
                
        return q2
        
#########################################
# Question:        
# Given a binary tree, 
# return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).
# For example:
# Given binary tree [3,9,20,null,null,15,7],   
# return its level order traversal as:
# [
#  [3],
#  [9,20],
#  [15,7]
# ]
###########################################
# Note: 一定是一整层一个subq
# input: [1,2,3,4,null,null,5]
# correst output: [[1],[2,3],[4,5]]
# 而不是：[[1],[2,3],[4],[5]]
###########################################
# Solution:
# q1: BFS的队列，记录节点
# q2：按层记录节点值
# 
# 这里，level1记录当前层最后一个节点索引，level2记录下一层节点索引
# 即根据每次添加元素后队列的rear
# 每次front访问的，记录在subq中
# 当front = level1 时，将subq添加到q2中，level1 = level2
###########################################
# beats: 100%
###########################################