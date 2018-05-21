# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        slow = slow.next
        slow = self.reverseList(slow)
        
        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True
    
    def reverseList(self, head):
        cur = head
        p1 = cur.next
        head.next = None
        while p1:
            p2 = p1.next
            p1.next = cur
            cur = p1
            p1 = p2
            
        return cur

# Description
# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Solution 
# 法1： 存到数组中 - space: O(n)
# 法2： 用栈 - space: O(n/2)
# 法3： 用快慢指针法找到中间节点
#       反转后半链表
#       比较前半与后半链表
#       本程序用的法3
# Note: 反转后最后一个节点的next要人为置为None
# Beats: 89.56%
# Runtime: 88ms
# easy
