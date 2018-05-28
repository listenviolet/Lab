class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 
        slow = nums[0]
        fast = nums[0]
        entry = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        while slow != entry:
            slow = nums[slow]
            entry = nums[entry]
        return entry

# Description:
# Given an array nums containing n + 1 integers 
# where each integer is between 1 and n (inclusive), 
# prove that at least one duplicate number must exist. 
# Assume that there is only one duplicate number, 
# find the duplicate one.

# Example 1:

# Input: [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: [3,1,3,4,2]
# Output: 3
# Note:

# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, 
# but it could be repeated more than once.
#################################################

# Solution:
# Floyd's Tortoise and Hare (Cycle Detection)
# See: 142-Linked List Cycle II
# 有重复元素表示按照如下方式走，会有相遇，
# 路径中环的entry即为重复元素
# slow = nums[slow]
# fast = nums[nums[fast]]

# 参见142题解：
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

# Beats: 99.73%
# Runtime: 40ms
# medium