# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        carry = 0
        tail = p1
        while p1 is not None and p2 is not None:
            cnt = p1.val + p2. val + carry
            p1.val = cnt % 10
            carry = cnt // 10
            tail = p1
            p1 = p1.next
            p2 = p2.next
        
        if p2 is not None:
            tail.next = p2
            tail = tail.next
            p1 = tail
            
        while p1 is not None:
            cnt = p1.val + carry
            print(carry, p1)
            p1.val = cnt % 10
            carry = cnt // 10
            tail = p1
            p1 = p1.next
            
        if carry > 0:
            tail.next = ListNode(carry)
            tail = tail.next
            tail.next = None
        return l1

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
# 这里用链表结点相加计算，将l1,l2的和加到l1中。
# 考虑链表长度：l1 < l2：将l1的尾指针指向l2--将来并入l1
#               l1 >= l2: 继续在l1运算
# 考虑最后一位进位：加入新的进位结点。
#                   由于p1最后一定指向None而不能指向进位结点，
#                   故用tail指针标记每次的尾结点，
#                   tail.next = ListNode(carry)使得l1与进位结点相连接


# Beats: 95.42%
# Runtime: 108ms
# medium