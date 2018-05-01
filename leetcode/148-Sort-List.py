# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeLists(self, l1, l2):
            # print("inmerge", l1.val, l2.val)
            dummy = ListNode(-1)
            p = dummy
            while(l1 is not None and l2 is not None):
                # print("in while:",l1.val, l2.val)
                if l1.val < l2.val:
                    # print("l1.val < l2.val")
                    p.next = l1
                    l1 = l1.next
                else:
                    # print("l1.val >= l2.val")
                    p.next = l2
                    l2 = l2.next
                p = p.next
            if l1 is not None: p.next = l1
            if l2 is not None: p.next = l2
            # print("dummy.next.val:",dummy.next.val)
            return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None: return head
        
        fast, slow = head, head
        while(fast.next is not None and fast.next.next is not None):
            fast = fast.next.next
            slow = slow.next
        fast = slow
        slow = slow.next
        fast.next = None
        
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.mergeLists(l1, l2)

# Question:
# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Solution:
# 表面上看，能够有O(n lgn)时间复杂度的算法为，
# 快速排序，堆排序，归并排序，
# 三者的空间复杂度分别为O(1), O(N),O(N)
#
# 针对数组而言，归并排序的空间复杂度为O(N), 
# 你需要开出O(N)的额外空间来容纳数组，来表示归并后的顺序。
# 但是，对于链表而言，你可以省下这部分空间的开销，
# 你只需要改变节点的next指针的指向，
# 就可以表示新的归并后的顺序了，
# 所以空间复杂度陡然降到了O(1)。


# 实践证明快速排序的速度比归并排序的速度更快,原因：
#
# 如果待排序的元素存储在数组中，
# 那么快速排序相对归并排序就有两个原因更快。
# 一是，可以很快地进行元素的读取
# (相对于链表，数组的元素是顺序摆放的，而链表的元素随机摆放)，
# 数组的partion这步就比链表的partion这步快。
# 二是，归并排序在merge阶段需要辅助数组，需要申请O(N)的空间，
# 申请空间也是需要时间的。
# 而快排不需要额外申请空间。
# 如果待排序的元素存储在链表中，快排的优点就变成了缺点。
# 归并排序于是就速度更优了。

# Beats: 48.36%
# medium
    
          
        