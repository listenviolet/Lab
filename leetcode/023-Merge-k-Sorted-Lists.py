# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge(l1, l2):
            if l1 == l2: return l1
            else:
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
        
        k = len(lists)
        if k == 0: return None
        elif k == 1: return lists[0]
        #elif k == 2: return merge(lists[0], lists[1])
        else:
            l1 = self.mergeKLists(lists[0:k//2])
            l2 = self.mergeKLists(lists[k//2:k])
            return merge(l1, l2)
            