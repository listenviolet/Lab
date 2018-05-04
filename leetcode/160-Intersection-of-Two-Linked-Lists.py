# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getListLen(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                headB = headB.next
        
        while(headA is not None and headB is not None):
            if headA is headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return 

# Description:
# Write a program to find the node at which 
# the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.


# Solution:
# 假设两个链表有交叉，那么交叉后的长度是一样的，
# 而交叉前的长度可能不一致。
# 如果我们将两个链表的交叉前的长度截成一致，
# 那么就可以同时遍历两个链表，判断是否有相交节点。
# 截断交叉前的不同长度等价于截断两个完整链表的不同长度。
# 此方法需要计算两个链表长度。

# Beats: 71.79%
# Runtime: 369ms
# easy
