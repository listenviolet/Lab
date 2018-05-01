# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
      
        # sol 3:
        # in-place
        # time O(n log n) space O(n)
        # runtime: 110ms
        if not head:
            return head
        res = []
        node = head
        while node: # O(n)
            res.append(node.val)
            node = node.next
        res.sort() # O(n log n)
        # node = head
        node = head
        for i in res:
            node.val = i
            node = node.next
        return head

# Beats: 99.45%
# medium