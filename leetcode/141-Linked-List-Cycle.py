# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None: return False
        
        node = head
        while(node is not None):
            if node.next == head:
                return True
            
            temp = node.next
            node.next = head
            node = temp
        return False

# Question:
# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# Solution:
# 如果链表中没有环，那么在遍历的过程中最后一个元素会指向空地址。
# 但是如果单纯的使用遍历法，当存在环的时候，会进入死循环==所以要想办法解决这个问题。
# 我们可以在遍历过程中将每个元素都指向head，
# 这样如果不存在环，就会有空指针，
# 如果存在环，最终会指向head而结束。
# Beats: 93.25%
# easy