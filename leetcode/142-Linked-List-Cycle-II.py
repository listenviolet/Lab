# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return 
        
        slow = head
        fast = head
        entry = head
        
        while(fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return entry
        return

# Question:
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?

# Solution:
# 1. 用slower和faster方法判断是否有环；
# 2. 设链表的头节点是head，
#    环的入口节点是entry, 
#    slower和 faster 2个指针相遇的节点是meeting;
# 3. 设L1是head到entry的正向距离，
#    L2是entry到meeting的正向距离，
#    C是环的长度，
#    n是faster指针在cycle里遍历的次数(不到一遍算0)；

# 根据上面的定义，可知：

# 1. 当slower和faster相遇时，
#    slower已经走了L1 + L2的距离，
#    也即head和meeting的距离;
# 2. 当slower和faster相遇时，faster已经走了L1 + L2 + n * C的距离;
# 3. 因为slower步进1，而faster步进2,
#    那么当slower和faster第一次相遇时，
#    faster已经走的距离是slower已经走的距离的两倍，
#    即 2* (L1 + L2) = L1 + L2 + n * C 
#    => L1 = (n - 1) * C + (C - L2)

# L1 = (n - 1) * C + (C - L2) 这个等式表明， 
# head和entry的距离(L1)，等于meeting到entry的正向距离
# （链表是有遍历方向的）。

# 这是因为式子中的 (n - 1) * C相当于走n-1个循环，
# 对一个指向meeting的环内指针来说，走(n - 1) * C等于回到起点，
# 所以式子可以简化成 L1 = C - L2。

# Beats: 79.41%
# medium