# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if not headA or not headB:
            return 
        p, q = headA, headB
        
        while p and q and p is not q:
            p = p.next
            q = q.next
            if p is q:
                return p
            if not p:
                p = headB
            if not q:
                q = headA
        return p

# Solution:
# 可以定义两个指针，让它们都将两个链表都遍历一遍，
# 那么它们走的总长度是一样的，
# 倘若两个链表相交，那么这两个指针一定会在某个地方相等。

# Beats: 4.32%
# Runtime: 519ms
# easy