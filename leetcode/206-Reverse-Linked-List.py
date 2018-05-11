# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None: return head
        cur = head
        p = head.next
        n = p.next
        while(n is not None):
            p.next = cur
            cur = p
            p = n
            n = p.next
        p.next = cur
        head.next = None
        head = p
        return head

# Description
# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Solution:
#         O -> O -> O -> O -> O -> None
#         |
#         head
#         |    |    |
#         cur  p    n

#         O<-> O    O -> O -> O -> None 
#              |    |    |
#              cur  p    n

#         O<-> O <- O    O -> O -> None 
#                   |    |    |
#                   cur  p    n

#         O<-> O <- O <- O    O -> None 
#                        |    |    |
#                        cur  p    n

# None <- O <- O <- O <- O <- O
#                        |    | 
#                        cur  p
#                             |
#                             head

# Beats: 99.86%
# Runtime: 40ms
# easy
