# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        new_node = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                new_val = l1.val
                new_node.next = ListNode(new_val)
                l1 = l1.next
                new_node = new_node.next
            else:
                new_val = l2.val
                new_node.next = ListNode(new_val)
                l2 = l2.next
                new_node = new_node.next
        
        if l1 == None:
            new_node.next = l2
        else:
            new_node.next = l1
        return dummy.next