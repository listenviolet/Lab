# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getInteger(l):
            res = 0
            cnt = 1
            while l is not None:
                res = res + l.val * cnt
                cnt *= 10
                l = l.next
            return res
        sum_integer = getInteger(l1) + getInteger(l2)
        if sum_integer == 0:
            return ListNode(0)
        
        head = ListNode(0)
        l = head
        while sum_integer > 0:
            l.next = ListNode(sum_integer % 10)
            l = l.next
            sum_integer /= 10
        return head.next

# Description:
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, 
# except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Solution:
# 这个解法也许不是出题人希望的正规解法
# 先将linked list表示的数，用整数表示，
# 然后整数相加，将所得和，用%/分解，表示成linked list形式。
# Notice:
# 这里注意，所得和为0的情况要单独讨论。
        
# Beats: 94.47%
# Runtime: 68ms
# medium